from flask import Flask, request, render_template
import cv2
import numpy as np
from skimage.feature import hog
from sklearn.preprocessing import StandardScaler
import joblib
import os
import tempfile
import shutil

app = Flask(__name__)

# Load the saved scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('svm_rbf_model.pkl')

# Define a temporary directory for processing
TEMP_UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = TEMP_UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(TEMP_UPLOAD_FOLDER):
    os.makedirs(TEMP_UPLOAD_FOLDER)

# Function to preprocess the image (same as notebook pipeline)
def preprocess_image(image_path):
    # Scale and pad to 128x128
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    h, w = img.shape
    target_size = (128, 128)
    aspect_ratio = w / h
    target_aspect = target_size[0] / target_size[1]
    if aspect_ratio > target_aspect:
        new_w = target_size[0]
        new_h = int(target_size[0] / aspect_ratio)
    else:
        new_w = int(target_size[1] * aspect_ratio)
        new_h = target_size[1]
    new_w = min(new_w, target_size[0])
    new_h = min(new_h, target_size[1])
    if new_w <= 0 or new_h <= 0:
        return None
    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    top = (target_size[1] - new_h) // 2
    bottom = target_size[1] - new_h - top
    left = (target_size[0] - new_w) // 2
    right = target_size[0] - new_w - left
    padded = cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)

    # Apply mild sharpening
    blurred = cv2.GaussianBlur(padded, (5, 5), 0)
    sharpened = cv2.addWeighted(padded, 1.5, blurred, -0.5, 0)

    # Extract HOG features
    features, _ = hog(
        sharpened,
        orientations=9,
        pixels_per_cell=(16, 16),
        cells_per_block=(2, 2),
        visualize=True
    )
    return features

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    confidence = None
    image_path = None
    error = None

    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            error = 'No file uploaded.'
        else:
            file = request.files['file']
            if file.filename == '':
                error = 'No file selected.'
            elif not file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                error = 'Invalid file format. Please upload a JPG, JPEG, or PNG image.'
            else:
                # Use a temporary file to avoid permanent storage
                temp_dir = tempfile.mkdtemp()
                try:
                    filename = 'uploaded_image.jpg'
                    filepath = os.path.join(temp_dir, filename)
                    file.save(filepath)

                    # Preprocess the image
                    features = preprocess_image(filepath)
                    if features is None:
                        error = 'Could not process the image. Please try another image.'
                    else:
                        # Scale the features
                        features_scaled = scaler.transform([features])

                        # Predict the emotion and confidence
                        prediction_probs = model.predict_proba(features_scaled)[0]
                        predicted_class = model.predict(features_scaled)[0]
                        confidence = max(prediction_probs) * 100
                        prediction = predicted_class

                        # Resize the image for display
                        display_img = cv2.imread(filepath)
                        h, w = display_img.shape[:2]
                        max_size = 400
                        if max(h, w) > max_size:
                            scale = max_size / max(h, w)
                            new_h, new_w = int(h * scale), int(w * scale)
                            display_img = cv2.resize(display_img, (new_w, new_h), interpolation=cv2.INTER_AREA)
                            cv2.imwrite(filepath, display_img)

                        # Copy the resized image to the static folder for display
                        display_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                        shutil.copy(filepath, display_path)
                        image_path = display_path

                finally:
                    # Clean up: remove the temporary directory and its contents
                    if os.path.exists(temp_dir):
                        shutil.rmtree(temp_dir)

    return render_template('index.html', prediction=prediction, confidence=confidence, image_path=image_path, error=error)

if __name__ == '__main__':
    app.run(debug=True)