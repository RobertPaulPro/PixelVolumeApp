from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    num3 = float(request.form['num3'])

    result1 = (num1 * num2)

    result2 = num3/result1

    if num1 != 0:
        result3 = math.sqrt(result2)

    answerx = num1 * result3
    answery = num2 * result3

    return render_template('result.html', answerx=answerx, answery=answery)

if __name__ == '__main__':
    app.run(debug=True)