# Cat Emotion Detector
I’m Anh Huynh, and I’m working on this AI project to figure out cat emotions—happy, sad, or angry—using SVM and Random Forest models. I got the idea after seeing how tricky it can be for owners to read their cats, like my friends who are always confused if their cat’s purring means happy or annoyed! I also read an article by Daniel Lavelle (2025) about his skittish kitten Split, which showed me how much owners want to understand their cats better. My goal’s to help pet owners get their cats’ moods with a simple web demo, so they can respond in the moment like giving a scared cat some space or cheering up a sad one. I think this can help cats feel less stressed and make owners feel closer to their pets, maybe even help vets spot stress during checkups.

## Datasets
- **Sources**:
  - [CATS, 2023](https://universe.roboflow.com/cats-xofvm/cat-emotions) on Roboflow: 670+ images of cats with emotions labeled.
  - [Cat Emotion Classification, 2024](https://universe.roboflow.com/cat-emotion-classification/cat-emotions-cgrxv) on Roboflow: 2,000+ images of cats with emotions labeled.
  - [Tanwar, 2023](https://www.kaggle.com/datasets/anshtanwar/pets-facial-expression-dataset) on Kaggle: 1,000 pet images, filtered to cats labeled happy, sad, angry.
- **Content**: 616 cat pics after filtering: 125 happy, 178 sad, 313 angry.
- **Preprocessing**: Resized to 64x64 pixels, converted to grayscale, HOG features extracted (648 features per image to highlight stuff like ears and whiskers).

## Vocabulary and Features 
- **Emotions**:
  - **Happy**: Relaxed posture, ears forward, eyes half-closed, whiskers forward [Bradshaw, 2016; Quaranta et al., 2020].
  - **Sad**: Crouched posture, ears slightly back, eyes slightly open, whiskers pulled back [Quaranta et al., 2020].
  - **Angry**: Arched back, ears flattened, eyes wide-open, whiskers pulled back, mouth open (hissing) [Quaranta et al., 2020].
- **Features Used**: Ear position, eye shape, whisker position, overall posture (e.g., ear angle captured via HOG features).

## Models
- **Type**: SVM (RBF kernel, C=10, gamma=0.1) and Random Forest (to be trained).
- **Training**: Trained on the 616 cat images described above.
- **Features**: Ear position, eye shape, whiskers, posture (extracted via HOG).
- **Status**: In progress - SVM got 68% accuracy in Iteration 0; Random Forest training and model comparison are next.

## Data Access 
- The dataset is private and stored locally on my computer while I’m working on it.
- Contact me at [huynhanh291195@gmail.com](mailto:huynhanh291195@gmail.com) if you want access, and I’ll share once it’s ready (it’ll go public on this repo after I’m done).
- Metadata (like “616 images, resized to 64x64”) will stay in this `README.md` and my Jupyter Notebook, even if the dataset isn’t available later.

## Dataset Structure
- **Images**: Stored in folders: `Cat Emotions.v1-test.folder`, `Cat Emotions.v2i.folder`, `CatDatasetKaggle` (PNG, JPG, JPEG formats).
- **Labels**: In `master_dataset_labels_v2.csv` with relative paths (e.g., `Cat Emotions.v1-test.folder/train/angry/cat1.jpg, angry`).
- **Model Outputs**: Will be in JSON format (e.g., `{"image": "cat1.jpg", "prediction": "Angry", "confidence": 0.85}`) once training is complete.

## References 
- Bradshaw, J. W. S. (2016). Sociality in cats: A comparative review. *Journal of Veterinary Behavior*, 11, 113–124. https://doi.org/10.1016/j.jveb.2015.09.004  
- Feighelstein, M., Shimshoni, I., Finka, L. R., Luna, S. P. L., Mills, D. S., & Zamansky, A. (2022). Automated recognition of pain in cats. *Scientific Reports*, 12, Article 9575. https://doi.org/10.1038/s41598-022-13348-1  
- Lavelle, D. (2025, March 30). She treats everyone with a deep growl: Can you train an angry cat to be more sociable? *The Guardian*. https://www.theguardian.com/lifeandstyle/2025/mar/30/she-treats-everyone-with-a-deep-growl-can-you-train-an-angry-cat-to-be-more-sociable  
- Quaranta, A., d’Ingeo, S., Amoruso, R., & Siniscalchi, M. (2020). Emotion recognition in cats. *Animals*, 10(7), Article 1107. https://doi.org/10.3390/ani10071107  
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., ... & Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, Article 160018. https://doi.org/10.1038/sdata.2016.18  
- CATS. (2023). Cat Emotions Dataset [Data set]. Roboflow Universe. https://universe.roboflow.com/cats-xofvm/cat-emotions  
- Cat Emotion Classification. (2024). Cat Emotions Dataset [Data set]. Roboflow Universe. https://universe.roboflow.com/cat-emotion-classification/cat-emotions-cgrxv  
- Tanwar, A. (2023). Pet’s Facial Expression Image Dataset [Data set]. Kaggle. https://www.kaggle.com/datasets/anshtanwar/pets-facial-expression-dataset  
