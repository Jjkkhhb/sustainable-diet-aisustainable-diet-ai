import pandas as pd
import pickle

# Load trained model

with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)

def food_recommendation(bmi):

    data = pd.read_csv("dataset/food_data.csv")

    prediction = model.predict([[bmi]])

    category = prediction[0]

    result = data[data["Category"] == category]

    foods = result.to_dict(orient="records")

    return foods