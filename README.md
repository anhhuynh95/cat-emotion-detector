
# 🐱 Cat Emotion Detector

Hi, I’m **Anh Huynh**. This project is about building an AI-based tool to detect **cat emotions** — specifically: **happy**, **sad**, or **angry** — using **SVM** and **Random Forest** classifiers.

The idea came from how often cat owners misread their pets. A friend once asked if purring meant their cat was happy or annoyed — it depends! After reading Daniel Lavelle's story about his anxious kitten Split (The Guardian, 2025), I wanted to help owners better understand their cats.

The goal: **a simple web demo** that predicts a cat’s mood from an image so owners can respond better (e.g., give a scared cat space, or comfort a sad one). This could also help vets assess stress during checkups.

---

## 📁 Project Structure (as seen on GitHub)

| File / Folder               | Description                                                |
|----------------------------|------------------------------------------------------------|
| `CatEmotionDetector.ipyn,CatEmotionDetector_I1.ipynb, CatEmotionDetector_I2.ipynb` | Jupyter notebook for each iteration (0 to 2) with updated dataset, images preprocessing, and models traning/evaluation |
| `app.py`                   | Flask app for local demo (in progress)                     |
| `static/` and `templates/` | Folders for images and HTML templates for Flask            |
| `README.md`                | You’re reading it!                                         |
| `.gitignore`               | Prevents large files (datasets, models) from being tracked |
| `LICENSE.txt`              | Creative Commons license (CC BY-NC 4.0)                    |

> 🔒 Note: All datasets, CSVs, and model `.pkl` files have been removed from Git tracking. You’ll need to request them (see below).

---

## 🧠 Models

| Model          | Status        | Accuracy | Description                                        |
|----------------|---------------|----------|----------------------------------------------------|
| SVM (RBF)      | ✅ Final Model | **~80%** | `C=10`, `gamma='scale'`, trained on 1,200 images after augmentation |
| Random Forest  | ✅ Trained     | 63%     | Underperforming SVM due to overfitting on high-dimensional HOG features         |

- **Features**: HOG (Histogram of Oriented Gradients)  
- **Preprocessing**: Resized to 128x128, grayscale, mild sharpening  
- **Extracted features**: ~1,764 per image

---

## 🐾 Emotions and Visual Features

| Emotion | Visual Cues                                                                 |
|---------|------------------------------------------------------------------------------|
| Happy   | Relaxed body, forward ears, half-closed eyes, forward whiskers              |
| Sad     | Crouched body, ears slightly back, eyes slightly open, whiskers pulled back |
| Angry   | Arched back, flattened ears, wide eyes, pulled whiskers, open mouth         |

> Sources: Bradshaw (2016), Quaranta et al. (2020)

---

## 📊 Dataset Info

| Source | Description |
|--------|-------------|
| **CATS (Roboflow, 2023)** | 670+ labeled cat emotion images |
| **Cat Emotion Classification (Roboflow, 2024)** | 2,000+ labeled images |
| **Tanwar (Kaggle, 2023)** | 1,000 pet images (filtered to 223 cat images) |
| **Stakeholders** | ~100 cat emotion images collected from different stakeholders (catowners) |

- **Used images after cleaning**: 616  
  → 125 happy, 178 sad, 313 angry  
- **After augmentation**: 1,200 images (400 per emotion)

### 🧼 Preprocessing:
- Resize to `128x128`, keep aspect ratio
- Grayscale + sharpening
- HOG feature extraction
- Labels stored in `master_dataset_labels_v2.csv` (not on GitHub)

---

## 📂 Dataset Folder Structure (Local)

```
📁 CatDatasetKaggle/
📁 Cat Emotions.v1-test.folder/
📁 Cat Emotions.v2i.folder/
📁 ImageCollection/
📄 master_dataset_labels_v2.csv
```

---

## 📬 Data Access

- 🔒 **Not included in GitHub**: image datasets, CSV labels, and model files (`.pkl`) are **stored locally** to avoid bloat and protect licensed data.
- 📧 Want to try the model or run the notebook?  
  Contact me at **huynhanh291195@gmail.com**, and I’ll share a ZIP with:
  - Labeled images
  - `master_dataset_labels_v2.csv`
  - Pretrained model: `svm_rbf_model.pkl`
  - Scaler: `scaler.pkl`

---

## ⚙️ Running the Notebooks

If you’ve received the dataset and model files:

1. Unzip into the same folder as the notebook.
2. Make sure your structure looks like this:
   ```
   ├── CatEmotionDetector_I2.ipynb
   ├── master_dataset_labels_v2.csv
   ├── CatDatasetKaggle/
   ├── Cat Emotions.v1-test.folder/
   ├── Cat Emotions.v2i.folder/
   ├── ImageCollection/
   ```
3. Install dependencies:
   ```bash
   pip install scikit-learn matplotlib opencv-python numpy
   ```
4. Run the notebook (Jupyter, VS Code, or Google Colab).

---

## 🌐 Flask Web App (Demo)

The `app.py` and related folders set up a small web demo:
- Upload an image of your cat
- See a prediction like:
  ```
  Your cat is happy, 63.77% sure!
  ```

> Currently works locally — future goal is to deploy it online.

---

## 🔄 FAIR Principles (Findable, Accessible, Interoperable, Reusable)

This project aligns with the [FAIR principles](https://doi.org/10.1038/sdata.2016.18):

| Principle | How It's Met |
|-----------|--------------|
| **Findable** | GitHub repo is tagged and searchable; datasets have unique Roboflow & Kaggle links |
| **Accessible** | Standard HTTPS access; metadata remains even if raw files are removed |
| **Interoperable** | Formats: `.jpg`, , `.jpeg`, `.png`, `.csv`; vocab aligns with cat behavior literature |
| **Reusable** | License: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/); all steps documented in code + notebook |

---

## 📚 References

- Bradshaw, J. W. S. (2016). Sociality in cats: A comparative review. Journal of Veterinary Behavior, 11, 113–124. https://doi.org/10.1016/j.jveb.2015.09.004
- Calvo, G., Holden, E., Reid, J., Scott, E. M., Firth, A., Bell, A., Robertson, S., & Nolan, A. M. (2014). Development of a behavior-based measurement tool with defined intervention level for assessing acute pain in cats. Journal of Small Animal Practice, 55(12), 622–629. https://doi.org/10.1111/jsap.12280
- Feighelstein, M., Shimshoni, I., Finka, L. R., Luna, S. P. L., Mills, D. S., & Zamansky, A. (2022). Automated recognition of pain in cats. Scientific Reports, 12, Article 9575. https://doi.org/10.1038/s41598-022-13348-1
- Finka, L. R., Luna, S. P. L., Mills, D. S., & Ward, J. M. (2019). Geometric morphometrics for the study of facial expressions in non-human animals, using the domestic cat as an exemplar. Scientific Reports, 9, Article 9883. https://doi.org/10.1038/s41598-019-46330-5
- Holden, E., Calvo, G., Collins, M., Bell, A., Reid, J., Scott, E. M., & Nolan, A. M. (2014). Evaluation of facial expression in acute pain in cats. Journal of Small Animal Practice, 55(12), 615–621. https://doi.org/10.1111/jsap.12283
- Merola, I., & Mills, D. S. (2016). Behavioural signs of pain in cats: An expert consensus. PLoS ONE, 11(2), Article e0150040. https://doi.org/10.1371/journal.pone.0150040
- Quaranta, A., d’Ingeo, S., Amoruso, R., & Siniscalchi, M. (2020). Emotion recognition in cats. Animals, 10(7), Article 1107. https://doi.org/10.3390/ani10071107
- Reid, J., Scott, E. M., Calvo, G., & Nolan, A. M. (2017). Definitive Glasgow acute pain scale for cats: Validation and intervention level. Veterinary Record, 180(18), 444–446. https://doi.org/10.1136/vr.104208
- GOFAIR (n.d.). FAIR Principles. https://www.go-fair.org/fair-principles/
- Lavelle, D. (2025, March 30). She treats everyone with a deep growl: Can you train an angry cat to be more sociable? The Guardian. https://www.theguardian.com/lifeandstyle/2025/mar/30/she-treats-everyone-with-a-deep-growl-can-you-train-an-angry-cat-to-be-more-sociable
- Sylvester.ai. (n.d.). How Sylvester works. https://www.sylvester.ai/how-sylvester-works
- CATS. (2023). Cat Emotions Dataset. Roboflow Universe. https://universe.roboflow.com/cats-xofvm/cat-emotions
- Cat Emotion Classification. (2024). Cat Emotions Dataset. Roboflow Universe. https://universe.roboflow.com/cat-emotion-classification/cat-emotions-cgrxv
- Ansh Tanwar (2023). 🐶Pet's Facial Expression Image Dataset😸. Kaggle. https://www.kaggle.com/ds/3546787
- University of Amsterdam. (2024, March 21). Onze mensen over… de rechten van dieren en de natuur [Our People on… the Rights of Animals and Nature]. Faculty of Law News. https://www.uva.nl/shared-content/faculteiten/nl/faculteit-der-rechtsgeleerdheid/nieuws/2024/03/onze-mensen-over-de-rechten-van-dieren-en-de-natuur.html 


---

## 🧑‍💻 Author

**Anh Huynh**  
📧 huynhanh291195@gmail.com  
🔗 [GitHub Repo](https://github.com/anhhuynh95/cat-emotion-detector)
