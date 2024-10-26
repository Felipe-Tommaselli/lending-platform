import numpy as np
import json

# Gerando os dados
np.random.seed(42)
credito_disponivel = np.random.uniform(0, 10000, 100)
saldo_em_conta = np.random.uniform(0, 10000, 100)
dividas = np.random.uniform(0, 10000, 100)

# Calculando o rótulo y com base em uma lógica simples
y = (
    (credito_disponivel * 0.7 + saldo_em_conta * 0.2 - dividas * 0.5) > 0
).astype(int)

# Montando a estrutura X e y
data = {
    "X": np.column_stack((credito_disponivel, saldo_em_conta, dividas)).tolist(),
    "y": y.tolist()
}

# Salvando em um arquivo JSON
output_path = "loan_data.json"
with open(output_path, "w") as f:
    json.dump(data, f, indent=4)