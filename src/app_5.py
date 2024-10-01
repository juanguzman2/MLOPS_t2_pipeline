import uvicorn
from fastapi import FastAPI, File, UploadFile
from io import StringIO
import pandas as pd
from joblib import load
import os

# Create the app object
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello"}

@app.post("/predict")
async def predict_diabetes(file: UploadFile = File(...)):
    # Load the model
    model_path = './models/best_random_forest_model.joblib'
 
    classifier = load(model_path)
    
    # Load feature names
    features_df = pd.read_csv('..\\data\\processed\\selected_features.csv')
    features = features_df['0'].to_list()

    # Read the uploaded file and process it
    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode('utf-8')))
    
    try:
        df = df[features]  # Select only relevant features
    except KeyError:
        return {"error": "Uploaded file does not contain the required features."}

    # Predict
    predictions = classifier.predict(df)
    
    return {
        "predictions": predictions.tolist()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
