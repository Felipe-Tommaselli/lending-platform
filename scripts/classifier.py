import numpy as np
from sklearn.ensemble import RandomForestClassifier
import json

with open("loan_data.json", "r") as f:
    data = json.load(f)

X = np.array(data["X"])
y = np.array(data["y"])

# Treinamento do modelo
model = RandomForestClassifier()
model.fit(X, y)

# Função para prever risco
# Função para prever risco
def predict_risk(credit_score, balance, debt):
    prediction = model.predict([[credit_score, balance, debt]])
    return True if prediction[0] == 1 else False
