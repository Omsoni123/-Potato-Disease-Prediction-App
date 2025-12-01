# this api code ruuning the output we can see in postmen while running and sending the request from postmen

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO     # use to read byte data
from PIL import Image     # use to read the image
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
app = FastAPI()           # creating and calling the fast api  

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model_dir = r"C:\Users\Om Soni\OneDrive\Desktop\potato diecese prediction\models"
model_version = 1
model = load_model(os.path.join(model_dir, f"model_v{model_version}.keras"))
print("Model loaded successfully!")
CLASS_NAME=['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

@app.get("/ping")              # to call my ping fucntion        (.get) is used for reading the file 
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:                     # convert bytes to np.ndarray
    image = np.array(Image.open(BytesIO(data)))                           # it will read the image in pil   and covert the iamge into np .array
    return image

@app.post("/predict")                              # is used for prediction purpose
async def predict(                        #async is use to make sure multiple request are excuted perfectly
    file: UploadFile = File(...)            # this function is used to upload a file 
):
    image = read_file_as_image(await file.read())         # await is used with async to handel multiple request
    img_batch = np.expand_dims(image, 0)                   # it expand the dimanesion of array
    
    predictions = model.predict(img_batch)             # predicting the model 

    predicted_class = CLASS_NAME[np.argmax(predictions[0])]          # selecting the class na,e
    confidence = np.max(predictions[0])                              # predicting the confience level
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":

    uvicorn.run(app, host='localhost', port=8000)          #making the function run    # to see this just click the link and at last (/ping)
