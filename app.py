from flask import Flask, render_template, request
from utils.bmi import calculate_bmi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    weight = float(request.form['weight'])
    height = float(request.form['height'])

    bmi = calculate_bmi(weight, height)

    return render_template(
        'result.html',
        bmi=bmi
    )

if __name__ == '__main__':
    app.run(debug=True)