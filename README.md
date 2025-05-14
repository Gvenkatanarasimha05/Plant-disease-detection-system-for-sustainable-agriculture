# 🌿 Plant Disease Detection for Sustainable Agriculture(AICTE)
 [Streamlit](https://plant-disease-detection-for-sustainable-agriculture.streamlit.app/).  LIVE MODEL

This project leverages deep learning to identify plant leaf diseases from images, aiding farmers and agricultural professionals in promoting healthier crops and supporting sustainable agricultural practices.

## 🚀 Features

- 🌱 Upload a leaf image to detect plant diseases automatically.
- 📷 Supports various plant types including tomato, potato, grape, apple, and more.
- 🧠 Powered by a Convolutional Neural Network (CNN) trained on the PlantVillage dataset.
- 🌍 Encourages early detection and prevention for sustainable farming.

---

## 🛠️ How It Works

1. A user uploads an image of a plant leaf.
2. The image is preprocessed and passed into a trained CNN model.
3. The model returns the predicted class (healthy or diseased).
4. The result is displayed with the disease name.

---

## 📁 Project Structure

```
├── PDDS.keras                # Trained Keras model (downloaded from Google Drive)
├── app.py                   # Streamlit app script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

---

## 🔗 Google Drive Model

The trained model file `PDDS.keras` is too large to store directly in the repository.

To download it automatically from Google Drive, the app uses the `gdown` package. The model is fetched when you run the app for the first time.

Make sure to replace the placeholder Google Drive file ID with your actual file ID in the `app.py`.

---

## ✅ Installation & Usage

### 1. Clone the repository

```bash
git clone https://https://github.com/Gvenkatanarasimha05/Plant-disease-detection-system-for-sustainable-agriculture/git
cd Plant-disease-detection-system-for-sustainable-agriculture
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🧪 Model Details

- Input Size: 224x224 pixels
- Architecture: CNN (custom or based on pre-trained models)
- Classes: 38 different categories of healthy and diseased leaves
- Dataset: PlantVillage dataset

---

## 📷 Sample Predictions

| Image | Predicted Class |
|-------|-----------------|
| ![Screenshot 2025-05-14 224018](https://github.com/user-attachments/assets/01521d46-9d93-4402-9517-6d7654199e4c)
|Strawberry_Leaf_scorch|


---

## 🌱 Sustainable Impact

By enabling early and accurate disease detection, this tool supports:

- Reduced pesticide usage
- Improved crop yields
- Data-driven farming decisions

---


## 🤝 Contributions

Contributions are welcome! Open an issue or submit a pull request to help improve this project.
