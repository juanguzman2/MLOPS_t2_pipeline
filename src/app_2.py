# 1. Library imports
import uvicorn
from fastapi import FastAPI
import pandas as pd
from joblib import load
import os

# 2. Create the app object
app = FastAPI()

# 3. Load the model and data
model_path = './models/best_random_forest_model.joblib'
classifier = load(model_path)

X_train = pd.read_csv('..\\data\\processed\\X_train.csv')  # Load X_train data
features = pd.read_csv('..\\data\\processed\\selected_features.csv')
features = features['0'].to_list()
X_train = X_train[features]

@app.get("/")
def read_root():
    return {"message": "Hello"}

@app.post("/predict")
def predict_diabetes():
    predictions = classifier.predict(X_train)
    return {
        "predictions": predictions.tolist()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
