def sustainability_score(bmi):

    if bmi < 18.5:
        return "Medium Sustainability"

    elif bmi < 25:
        return "High Sustainability"

    else:
        return "Low Sustainability"