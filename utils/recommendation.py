import pandas as pd

def food_recommendation(bmi):

    data = pd.read_csv("dataset/food_data.csv")

    if bmi < 18.5:
        category = "Weight Gain"

    elif bmi < 25:
        category = "Normal"

    else:
        category = "Weight Loss"

    result = data[data["Category"] == category]

    foods = result.to_dict(orient="records")

    return foods