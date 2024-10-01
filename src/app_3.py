import uvicorn
from fastapi import FastAPI
from src.diabetes import DiabetesData
from joblib import load
import os

# Create the app object
app = FastAPI()

# Load the model
model_path = './models/best_random_forest_model.joblib'
classifier = load(model_path)

@app.get("/")
def read_root():
    return {"message": "Hello"}

@app.post('/predict')
def predict_diabetes(data: DiabetesData):
    input_data = [data.dict().values()]  # Extract all input values
    prediction = classifier.predict(input_data)
    return {
        'predictions': prediction.tolist()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
