# api/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import os, traceback

app = FastAPI()

# ---- CORS: allow for testing; in production set to your Streamlit domain only ----
# For local testing you can use ["*"], but restrict it when deployed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change to ['https://your-streamlit-app.streamlit.app'] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Config from environment (portable) ----
# Default values are for local dev. Change via env vars in production.
MODEL_DIR = os.environ.get("MODEL_DIR", "models")   # relative folder in repo
MODEL_VERSION = os.environ.get("MODEL_VERSION", "1")
MODEL_FILENAME = f"model_v{MODEL_VERSION}.keras"    # change to .h5 if that's your file
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

# Diagnostics: ensure path exists and list files
print("Using MODEL_PATH =", MODEL_PATH)
if not os.path.exists(MODEL_PATH):
    print("ERROR: Model file not found at:", MODEL_PATH)
    try:
        print("Files in model dir:", os.listdir(MODEL_DIR))
    except Exception as e:
        print("Could not list model dir:", e)
    # If you prefer the process to continue (and fail on request) comment out the next line
    raise FileNotFoundError(f"Model file missing at {MODEL_PATH}")

# Try loading the model and show any errors
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully from:", MODEL_PATH)
except Exception:
    print("Failed to load model — full traceback below:")
    traceback.print_exc()
    raise

CLASS_NAME = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

@app.get("/ping")
async def ping():
    return {"status": "alive"}

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)).convert("RGB"))
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # read bytes and convert to numpy
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    # prediction
    predictions = model.predict(img_batch)
    predicted_class = CLASS_NAME[int(np.argmax(predictions[0]))]
    confidence = float(np.max(predictions[0]))

    return {
        'class': predicted_class,
        'confidence': confidence
    }

# Only run uvicorn when executed directly (not when imported by hosting platforms)
if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)


