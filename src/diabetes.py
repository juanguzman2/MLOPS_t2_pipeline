from pydantic import BaseModel

# Clase que describe los datos de predicción de diabetes
class DiabetesData(BaseModel):
    Age: float
    Gender: float
    Polyuria: float
    Polydipsia: float
    sudden_weight_loss: float
    weakness: float
    Polyphagia: float
    Genital_thrush: float
    visual_blurring: float
    Itching: float
    Irritability: float
    delayed_healing: float
    partial_paresis: float
    muscle_stiffness: float
    Alopecia: float
    Obesity: float
