from flask import Flask, render_template, request
from utils.bmi import calculate_bmi
from utils.recommendation import food_recommendation
from utils.sustainability import sustainability_score
import matplotlib.pyplot as plt
import os
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/register')
def register_page():
    return render_template('register.html')
@app.route('/register')
def register_page():
    return render_template('register.html')
@app.route('/register', methods=['POST'])
def register():

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()

    return "Registration Successful"
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return render_template('index.html')

    else:
        return "Invalid Username or Password"

@app.route('/predict', methods=['POST'])
def predict():

    weight = float(request.form['weight'])
    height = float(request.form['height'])

    bmi = calculate_bmi(weight, height)
    foods = food_recommendation(bmi)
    score = sustainability_score(bmi)
    food_names = []
    calories = []

    for food in foods:
        food_names.append(food["Food"])
        calories.append(food["Calories"])

    plt.figure(figsize=(6,4))

    plt.bar(food_names, calories)

    plt.xlabel("Foods")
    plt.ylabel("Calories")

    plt.title("Calories Analysis")

    graph_path = "static/images/chart.png"

    plt.savefig(graph_path)

    plt.close()
    
    

    return render_template(
    'result.html',
    bmi=bmi,
    foods=foods,
    score=score
)

if __name__ == '__main__':
    app.run(debug=True)