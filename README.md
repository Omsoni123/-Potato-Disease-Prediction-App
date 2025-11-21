
# 🥔 Potato Disease Prediction App

## 🚀 Overview

An AI-powered web and API-based application designed to detect potato leaf diseases (Early Blight, Late Blight, Healthy). Built for farmers to enable early detection, reduce crop loss, and enhance agricultural productivity.

## 🌱 Real-World Impact

This project helps farmers by:

* Detecting diseases at an early stage.
* Reducing pesticide misuse through targeted treatment.
* Improving yield and overall crop health.
* Supporting data-driven agricultural decisions.

## 🌟 Features

* **FastAPI Backend:** TensorFlow CNN-based image classification.
* **User-Friendly Interface:** Streamlit + HTML UI.
* **REST API:** Efficient image preprocessing and prediction.
* **Optimized Performance:** CORS handling, async processing, efficient model loading.
* **Scalability:** Low latency real-time predictions.

## 🛠️ Tech Stack

* **Frontend:** Streamlit, HTML, CSS
* **Backend:** FastAPI, Python
* **ML Model:** TensorFlow CNN
* **Database:** SQLite / PostgreSQL (optional)
* **Deployment:** Docker, Cloud (AWS/GCP)

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

1. Upload a potato leaf image.
2. Model predicts the disease.
3. Result displayed instantly.

## 📊 Model Training

* Dataset collection
* Image preprocessing (resize, normalization, augmentation)
* CNN training using TensorFlow
* Hyperparameter tuning for improved accuracy

## 🔗 API Endpoints

| Method | Endpoint   | Description                               |
| ------ | ---------- | ----------------------------------------- |
| POST   | `/predict` | Upload image → returns disease prediction |
| GET    | `/health`  | Health status of API                      |

## 🔍 API Testing via Postman

1. Open Postman → New **POST** request.
2. URL: `http://127.0.0.1:8000/predict`
3. Body → **form-data** → key: `file` (type: File)
4. Upload an image.
5. Click **Send** to get prediction.
6. For health check: `GET http://127.0.0.1:8000/health`.

## 🚀 Future Improvements

* Cloud deployment
* Larger dataset for higher accuracy
* Multi-language interface

## 👨‍💻 Author

**Om Soni**
📧 [om.soni2706@gmail.com](mailto:om.soni2706@gmail.com)
🔗 GitHub: [https://github.com/Omsoni123](https://github.com/Omsoni123)
🔗 LinkedIn: [https://linkedin.com/in/om-soni-8b0643231](https://linkedin.com/in/om-soni-8b0643231)

## 📜 License

MIT License
