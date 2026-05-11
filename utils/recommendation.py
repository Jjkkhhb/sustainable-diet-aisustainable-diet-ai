def food_recommendation(bmi):

    if bmi < 18.5:
        return [
            "Banana Smoothie",
            "Peanut Butter Sandwich",
            "Oats with Milk",
            "Rice and Chicken"
        ]

    elif bmi < 25:
        return [
            "Vegetable Salad",
            "Brown Rice",
            "Eggs",
            "Fruits"
        ]

    else:
        return [
            "Green Salad",
            "Grilled Chicken",
            "Soup",
            "Oats"
        ]