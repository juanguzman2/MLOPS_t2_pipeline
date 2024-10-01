import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from joblib import load
import os
from src.diabetes import DiabetesData  # Importa la clase DiabetesData

# Crear la aplicación FastAPI
app = FastAPI()

# Cargar el modelo y los datos
model_path = './models/best_random_forest_model.joblib'
classifier = load(model_path)

# Cargar las características seleccionadas
features = pd.read_csv('./data/processed/selected_features.csv')
features_list = features['0'].to_list()  # Ya es una lista de características

@app.get("/")
def read_root():
    return {"message": "Hello"}

@app.post("/predict")
def predict_diabetes(data: DiabetesData):  # Recibe un objeto DiabetesData
    # Convertir los datos recibidos en un DataFrame de pandas
    input_data = pd.DataFrame([data.dict()])

    # Renombrar las columnas del input_data para que coincidan con las de selected_features
    rename_columns = {
        'sudden_weight_loss': 'sudden weight loss',
        'Genital_thrush': 'Genital thrush',
        'delayed_healing': 'delayed healing',
        'partial_paresis': 'partial paresis'
    }
    
    input_data = input_data.rename(columns=rename_columns)

    # Filtrar las columnas en el orden correcto utilizando la lista de características
    input_data = input_data[features_list]

    # Realizar la predicción
    prediction = classifier.predict(input_data)

    return {
        "prediction": int(prediction[0])  # Convertir a int para evitar problemas con JSON
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
