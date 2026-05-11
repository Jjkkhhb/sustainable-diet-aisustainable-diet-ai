from flask import Flask, render_template, request
from utils.bmi import calculate_bmi
from utils.recommendation import food_recommendation
from utils.sustainability import sustainability_score

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    weight = float(request.form['weight'])
    height = float(request.form['height'])

    bmi = calculate_bmi(weight, height)
    foods = food_recommendation(bmi)
    score = sustainability_score(bmi)
    
    

    return render_template(
    'result.html',
    bmi=bmi,
    foods=foods,
    score=score
)

if __name__ == '__main__':
    app.run(debug=True)