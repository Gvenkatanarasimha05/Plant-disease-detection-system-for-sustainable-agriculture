import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import gdown

# Google Drive file ID and output model path
file_id = "1Cg37sbW97P0sX3Y-3Um8NZgddi_QznJ6"
output_model_path = "PDDS.keras"

# Download the model if not already downloaded
if not os.path.exists(output_model_path):
    with st.spinner("📦 Downloading model from Google Drive..."):
        gdown.download(f"https://drive.google.com/uc?id={file_id}", output_model_path, quiet=False)

# Load the Keras model
model = tf.keras.models.load_model(output_model_path)

# Class names (Update these based on your dataset if needed)
class_names = [
    'Apple__Apple_scab', 'Apple_Black_rot', 'Apple_Cedar_apple_rust', 'Apple_healthy',
    'Blueberry_healthy', 'Cherry(including_sour)Powdery_mildew', 'Cherry(including_sour)healthy',
    'Corn(maize)Cercospora_leaf_spot Gray_leaf_spot', 'Corn(maize)Common_rust',
    'Corn_(maize)Northern_Leaf_Blight', 'Corn(maize)healthy', 'Grape_Black_rot',
    'GrapeEsca(Black_Measles)', 'GrapeLeaf_blight(Isariopsis_Leaf_Spot)', 'Grape_healthy',
    'OrangeHaunglongbing(Citrus_greening)', 'Peach_Bacterial_spot', 'Peach_healthy',
    'Pepper,bellBacterial_spot', 'Pepper,bellhealthy', 'Potato_Early_blight',
    'Potato_Late_blight', 'Potato_healthy', 'Raspberry_healthy', 'Soybean_healthy',
    'Squash_Powdery_mildew', 'Strawberry_Leaf_scorch', 'Strawberry_healthy',
    'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites Two-spotted_spider_mite',
    'Tomato_Target_Spot', 'Tomato_Tomato_Yellow_Leaf_Curl_Virus', 'Tomato_Tomato_mosaic_virus',
    'Tomato__healthy'
]

# Streamlit UI
# st.set_page_config(page_title="Plant Disease Detection", page_icon="🌿")
st.title("🌿 Plant Disease Detection using Deep Learning")
st.write("Upload an image of a *plant leaf, and the app will predict the **disease* using a trained model.")
st.write("This Model is not 100% Accurate")

# File uploader
uploaded_file = st.file_uploader("📷 Upload a leaf image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

# Prediction logic
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='🖼 Uploaded Image', use_column_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Model prediction
    with st.spinner("🔍 Predicting..."):
        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]

    st.success(f"✅ *Predicted Disease:* {predicted_class}")
