Heart Disease Prediction using Logistic Regression
====================================================

Project Overview
----------------
This project is a web application built with Flask that uses a Logistic Regression model to predict the likelihood of a person having heart disease based on their medical attributes. It aims to provide a simple and interactive interface for users to input key health metrics like age, cholesterol, and resting blood pressure to receive a real-time prediction about their risk.

Features
--------
- User-Friendly Web Interface: Clean and simple UI for data input.
- Real-Time Prediction: Get instant predictions from the trained machine learning model.
- Powered by Scikit-learn: Utilizes a Logistic Regression model for classification.
- Lightweight Backend: Built with the Flask web framework.

Technologies Used
-----------------
- Backend: Flask
- Machine Learning: Scikit-learn, Pandas, NumPy
- Frontend: HTML, CSS
- Programming Language: Python 3

Setup and Installation
----------------------
Follow these steps to get the project running on your local machine.

1. Prerequisites:
   - Python 3.7 or higher
   - Git

2. Clone the Repository:
   git clone https://github.com/SURESH6161/Logistic_alogrithm_heart_disease_find.git
   cd Logistic_alogrithm_heart_disease_find

3. Create a Virtual Environment:
   It's highly recommended to use a virtual environment.
   - For Windows: python -m venv venv && venv\Scripts\activate
   - For macOS/Linux: python3 -m venv venv && source venv/bin/activate

4. Install Dependencies:
   pip install -r requirements.txt
   (Note: If you don't have a requirements.txt file, create one with `pip freeze > requirements.txt` after installing libraries manually.)

5. Run the Application:
   python app.py

Usage
-----
1. Once the server is running, open your web browser.
2. Navigate to http://127.0.0.1:5000 (or the address shown in your terminal).
3. Fill in the required medical details in the input fields.
4. Click the "Predict Risk" button to see the prediction result.

Dataset
-------
The model was trained on the "Heart Disease UCI" dataset, which is a popular dataset for classification tasks. It contains 14 attributes including age, sex, chest pain type, cholesterol, and more.
- Source: UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/heart+Disease)

Model
-----
The prediction is performed by a Logistic Regression model, a reliable algorithm for binary classification. The trained model is saved as a .pkl file and loaded by the Flask application to make predictions.
(Note: You should add your model's accuracy to the file).

License
-------
This project is licensed under the MIT License.