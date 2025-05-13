import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
model = tf.keras.models.load_model("plant_disease_model.h5")

# Class names (make sure these match your model's output order)
class_names = ['Class1', 'Class2', 'Class3', '...']  # Replace with actual class names

# Title
st.title("🌿 Plant Disease Detection")
st.write("Upload an image of a plant leaf and this app will predict the disease.")

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess image
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    # Show result
    st.success(f"✅ Predicted Disease: **{predicted_class}**")
