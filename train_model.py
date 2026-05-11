import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Sample dataset

data = {
    "BMI": [16, 17, 18, 22, 23, 24, 27, 30, 35],
    "Category": [
        "Weight Gain",
        "Weight Gain",
        "Weight Gain",
        "Normal",
        "Normal",
        "Normal",
        "Weight Loss",
        "Weight Loss",
        "Weight Loss"
    ]
}

df = pd.DataFrame(data)

# Input and Output

X = df[["BMI"]]
y = df["Category"]

# Train model

model = DecisionTreeClassifier()

model.fit(X, y)

# Save model

with open("models/model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Trained Successfully")