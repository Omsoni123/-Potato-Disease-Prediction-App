# app/app.py
import os
import io
import requests
from PIL import Image
import streamlit as st

# Use env var in production; default to local for dev
API_URL = os.environ.get("PREDICT_API_URL", "http://127.0.0.1:8000/predict")

st.title("Potato Disease Prediction")
uploaded_file = st.file_uploader("Upload a potato leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        # Prepare bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="JPEG")
        image_bytes.seek(0)

        # Proper multipart/form-data file tuple
        files = {"file": ("leaf.jpg", image_bytes, "image/jpeg")}

        # Try calling API
        try:
            response = requests.post(API_URL, files=files, timeout=30)
        except requests.RequestException as e:
            st.error(f"Network error calling API: {e}")
            st.write("Tried API_URL:", API_URL)
        else:
            st.write("Raw API Response:", response.text)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if "class" in data and "confidence" in data:
                        st.success(f"Prediction: {data['class']}")
                        st.write(f"Confidence: {data['confidence']:.2f}")
                    else:
                        st.error("API response missing expected keys.")
                except Exception as e:
                    st.error(f"Error parsing response JSON: {e}")
            else:
                st.error(f"API request failed ({response.status_code}): {response.text}")


