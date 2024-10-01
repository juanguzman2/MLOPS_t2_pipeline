from pydantic import BaseModel, Field, conint, confloat
from typing import Literal

# Clase que describe los datos de predicción de diabetes
class DiabetesData(BaseModel):
    Age: confloat(gt=0)  # Edad debe ser un número mayor que 0
    Gender: Literal[0, 1]  # El género puede ser 0 (hombre) o 1 (mujer)
    Polyuria: Literal[0, 1]  # 0 para No, 1 para Sí
    Polydipsia: Literal[0, 1]  # 0 para No, 1 para Sí
    sudden_weight_loss: Literal[0, 1]  # 0 para No, 1 para Sí
    weakness: Literal[0, 1]  # 0 para No, 1 para Sí
    Polyphagia: Literal[0, 1]  # 0 para No, 1 para Sí
    Genital_thrush: Literal[0, 1]  # 0 para No, 1 para Sí
    visual_blurring: Literal[0, 1]  # 0 para No, 1 para Sí
    Itching: Literal[0, 1]  # 0 para No, 1 para Sí
    Irritability: Literal[0, 1]  # 0 para No, 1 para Sí
    delayed_healing: Literal[0, 1]  # 0 para No, 1 para Sí
    partial_paresis: Literal[0, 1]  # 0 para No, 1 para Sí
    muscle_stiffness: Literal[0, 1]  # 0 para No, 1 para Sí
    Alopecia: Literal[0, 1]  # 0 para No, 1 para Sí
    Obesity: Literal[0, 1]  # 0 para No, 1 para Sí
