# 1. Library imports
import uvicorn
from fastapi import FastAPI
from src.diabetes import DiabetesData
from joblib import load
import os

# 2. Create the app object
app = FastAPI()

# 3. Load the model
model_path = './models/best_random_forest_model.joblib'
classifier = load(model_path)

# 4. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted diabetes result
@app.post('/predict')
def predict_diabetes(data: DiabetesData):
    input_data = [data.dict().values()]  # Extracting all values at once
    prediction = classifier.predict(input_data)
    return {
        'predictions': prediction.tolist()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
