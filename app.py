import os
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the logistic regression model
print(f"os.getcwd(): {os.getcwd()}")
model = joblib.load('logistic_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get user input from form
        age = float(request.form['age'])
        bp = float(request.form['resting_bp'])
        cholesterol = float(request.form['cholesterol'])

        # Make prediction
        pred_num = model.predict([[age, bp, cholesterol]])[0]

        # Interpret result
        prediction = "Heart Disease Detected" if pred_num == 1 else "No Heart Disease"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
