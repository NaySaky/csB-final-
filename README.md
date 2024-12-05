
This repository provides a Grade Prediction Application designed to predict a student's final grade (G3) using Linear Regression and Random Forest models. The application features a Streamlit-based GUI for user-friendly interactions and detailed visualizations of the predictions and grade progressions.

Features
Streamlit GUI: Interactive interface for predicting grades based on user inputs.
Model Predictions: Leverages Linear Regression and Random Forest models to predict G3.
Visualization:
Bar charts comparing model predictions.
Line plots showcasing grade progression (G1 → G2 → G3).
Feature Importance Analysis: Insights into which features most influence the predictions.

Features
Streamlit GUI: Interactive interface for predicting grades based on user inputs.
Model Predictions: Leverages Linear Regression and Random Forest models to predict G3.
Visualization:
Bar charts comparing model predictions.
Line plots showcasing grade progression (G1 → G2 → G3).
Feature Importance Analysis: Insights into which features most influence the predictions.

1. Steps
Clone this repository:
git clone https://github.com/yourusername/grade-prediction-app.git
cd grade-prediction-app

2. Install the required dependencies:
pip install -r requirements.txt
Or 
pip3 install -r requirements.txt

3.Ensure the following files are in the root directory:
linear_model_class.joblib (Pre-trained Linear Regression model)
random_forest_model_class.joblib (Pre-trained Random Forest model)
student-mat.csv (Dataset for model training, if required)

How to Launch the Streamlit app:
streamlit run run.py
Or 
Python3 -m streamlit run run.py
