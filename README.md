# 🥔 Potato Disease Prediction App

## 🚀 Overview

An AI-powered web and API-based application designed to detect potato leaf diseases (Early Blight, Late Blight, Healthy). Built for farmers to enable early detection, reduce crop loss, and enhance agricultural productivity.

## 🌱 Real-World Impact

This project is actively helping farmers by providing an easy-to-use tool for early disease detection in potato crops. By leveraging AI, farmers can:

- Detect diseases in their crops at an early stage, preventing large-scale damage.
- Reduce pesticide overuse by applying targeted treatments only where needed.
- Improve overall yield and crop health, ensuring better profitability and sustainability.
- Make data-driven decisions to optimize their farming practices.

## 🌟 Features

- **FastAPI Backend:** Utilizes a TensorFlow CNN model for accurate image classification.
- **User-Friendly Interface:** Designed with Streamlit & HTML for seamless image uploads and real-time predictions.
- **REST API Integration:** Handles image preprocessing and predictions efficiently.
- **Optimized Performance:** Implemented CORS handling, asynchronous processing, and efficient model loading.
- **Scalability:** Supports real-time predictions with minimal latency.

## 🛠️ Tech Stack

- **Frontend:** Streamlit, HTML, CSS
- **Backend:** FastAPI, Python
- **Machine Learning Model:** TensorFlow CNN
- **Database (if applicable):** SQLite / PostgreSQL
- **Deployment:** Docker, AWS/GCP (optional)

## 📌 Installation

```bash
# Clone the repository
git clone https://github.com/Omsoni123/Potato-Disease-Prediction.git
cd Potato-Disease-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI backend
uvicorn app:app --host 0.0.0.0 --port 8000

# Run the Streamlit frontend
streamlit run app.py
```

## 🖼️ Usage

1. Upload an image of a potato leaf.
2. The model processes the image and predicts the disease type.
3. The result is displayed instantly, helping farmers make informed decisions.

## 📊 Model Training

- Collected a dataset of potato leaf images.
- Preprocessed the images (resizing, normalization, augmentation).
- Trained a **Convolutional Neural Network (CNN)** using TensorFlow.
- Optimized model accuracy through hyperparameter tuning.

## 🔗 API Endpoints

| Method | Endpoint     | Description                            |
|--------|-------------|----------------------------------------|
| `POST` | `/predict`  | Uploads an image and returns disease classification |
| `GET`  | `/health`   | Checks API health status |

## 🔍 API Testing via Postman

1. Open **Postman** and create a new **POST request**.
2. Enter the API endpoint: `http://127.0.0.1:8000/predict`
3. Go to the **Body** tab and select **form-data**.
4. Add a **key** named `file`, set type to **File**, and upload an image of a potato leaf.
5. Click **Send** to receive the prediction response.
6. For health check, send a **GET request** to `http://127.0.0.1:8000/health`.

## 🚀 Future Improvements

- Deploy model on cloud (AWS/GCP)
- Improve model accuracy with more training data
- Add multi-language support for wider accessibility

## 👨‍💻 Author

**Om Soni**  
📧 [om.soni2706@gmail.com](mailto:om.soni2706@gmail.com)  
🔗 [GitHub](https://github.com/Omsoni123) | [LinkedIn](https://linkedin.com/in/om-soni-8b0643231)

## 📜 License

This project is licensed under the MIT License.


