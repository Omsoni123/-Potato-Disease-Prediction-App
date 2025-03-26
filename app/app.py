import streamlit as st
import requests
import io
from PIL import Image

# Streamlit App Title
st.title("Potato Disease Prediction")

# File Uploader for Image
uploaded_file = st.file_uploader("Upload a potato leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display Uploaded Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        # Convert image to bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="JPEG")

        # Send image to API
        files = {"file": image_bytes.getvalue()}
        response = requests.post("http://127.0.0.1:8000/predict", files=files)

        # Debugging: Show raw response
        st.write("Raw API Response:", response.text)

        if response.status_code == 200:
            try:
                response_data = response.json()
                if "class" in response_data and "confidence" in response_data:
                    st.success(f"Prediction: {response_data['class']}")
                    st.write(f"Confidence: {response_data['confidence']:.2f}")
                else:
                    st.error("Error: API response does not contain expected keys.")
            except Exception as e:
                st.error(f"Error parsing response: {e}")
        else:
            st.error("Error: API request failed. Check FastAPI server.")
