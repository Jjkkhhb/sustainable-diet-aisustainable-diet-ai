import pandas as pd
import pickle
import os

# Base project directory

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Dataset path

csv_path = os.path.join(
    BASE_DIR,
    "dataset",
    "food_data.csv"
)

# Model path

model_path = os.path.join(
    BASE_DIR,
    "models",
    "model.pkl"
)

# Load dataset

data = pd.read_csv(csv_path)

# Load model

with open(model_path, "rb") as file:
    model = pickle.load(file)

# Recommendation function

def food_recommendation(bmi):

    prediction = model.predict([[bmi]])

    category = prediction[0]

    result = data[data["Category"] == category]

    foods = result.to_dict(orient="records")

    return foods