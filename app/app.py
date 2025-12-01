import streamlit as st
import requests
import io
from PIL import Image
import time

# Custom Styles
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #ff5733;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title with Styling
st.markdown("<p class='title'>🥔 Potato Disease Prediction 🍂</p>", unsafe_allow_html=True)

# File Uploader & Camera Input
st.markdown("## 📸 Upload or Capture Image")
option = st.radio("Choose Image Source:", ("Upload Image", "Use Camera"))

if option == "Upload Image":
    uploaded_file = st.file_uploader("📤 Upload a potato leaf image", type=["jpg", "png", "jpeg"])
else:
    uploaded_file = st.camera_input("📷 Capture Image")

if uploaded_file:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(uploaded_file, caption="📷 Uploaded Image", use_container_width=True)

    st.markdown("""
    <p style="text-align:center; font-size:18px; font-weight:bold;">✅ Click Predict to analyze the disease!</p>
    """, unsafe_allow_html=True)

    if st.button("🔍 Predict", use_container_width=True):
        with st.spinner("Analyzing Image... 🔄"):
            time.sleep(2)  # Simulating loading effect
            
            # Convert image to bytes
            image = Image.open(uploaded_file)
            image_bytes = io.BytesIO()
            image.save(image_bytes, format="JPEG")
            
            # Send image to API
            files = {"file": image_bytes.getvalue()}
            response = requests.post("http://127.0.0.1:8000/predict", files=files)
            
            # Debugging: Show raw response
            st.write("🛠 Raw API Response:", response.text)
            
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    if "class" in response_data and "confidence" in response_data:
                        st.success(f"🎯 Prediction: {response_data['class']}")
                        st.progress(response_data["confidence"])
                        st.write(f"🔹 Confidence: {response_data['confidence']:.2f}")
                    else:
                        st.error("⚠️ Error: Unexpected API response format.")
                except Exception as e:
                    st.error(f"❌ Error parsing response: {e}")
            else:
                st.error("🚨 API request failed. Check FastAPI server.")




