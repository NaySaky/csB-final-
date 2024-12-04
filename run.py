import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import matplotlib.pyplot as plt
import seaborn as sns

# Load pre-trained models
linear_model = load('linear_model_class.joblib')
random_forest_model = load('random_forest_model_class.joblib')

# Title
st.title("**Grade Prediction Application**")
st.markdown("""
    <h3 style="color: #3e5c6f;">Enter the values for G1, G2, absences, Medu, and higher_yes 
    to predict the final grade (G3) using Linear Regression and Random Forest models.</h3>
""", unsafe_allow_html=True)

# Spacing for clarity
st.markdown("___")

# User input for prediction
g1 = st.slider('G1 (Grade in first period)', min_value=0, max_value=20, step=1)
g2 = st.slider('G2 (Grade in second period)', min_value=0, max_value=20, step=1)
absences = st.slider('Absences', min_value=-90, max_value=0, step=1)
medu = st.selectbox('Mother\'s Education Level (Medu)', [0, 1, 2, 3])
higher_yes = st.selectbox('Student’s Higher Education (higher_yes)', ['Yes', 'No'])
higher_yes = 1 if higher_yes == 'Yes' else 0  # Convert to 1 or 0

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'G1': [g1],
    'G2': [g2],
    'absences': [absences],
    'Medu': [medu],
    'higher_yes': [higher_yes]
})

# Predict using both models
if st.button("**Predict Grade**"):
    st.write("**Running predictions...**")

    try:
        # Make predictions with both models
        linear_predictions = linear_model.predict(input_data)
        random_forest_predictions = random_forest_model.predict(input_data)

        # Display predictions with exact values
        st.markdown(f"### **Linear Regression Prediction**: {linear_predictions[0]:.2f}")
        st.markdown(f"### **Random Forest Prediction**: {random_forest_predictions[0]:.2f}")

        # First Chart: Comparison of Predictions (Bar Chart)
        st.write("### **Comparison of Predictions by Models**")

        # Create a DataFrame for the predictions
        predictions_df = pd.DataFrame({
            'Model': ['Linear Regression', 'Random Forest'],
            'Prediction': [linear_predictions[0], random_forest_predictions[0]]
        })

        # Improved color and chart layout for the first chart
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x='Model', y='Prediction', data=predictions_df, ax=ax, palette="Blues_d")
        ax.set_title("Predictions by Linear Regression and Random Forest", fontsize=18)
        ax.set_ylabel('Predicted Grade (G3)', fontsize=14)
        ax.set_ylim([0, 20])  # Limiting y-axis to grade range (0-20)
        
        # Annotating the bars with exact numbers for better user experience
        for i in range(len(predictions_df)):
            ax.text(i, predictions_df['Prediction'][i] + 0.2, f'{predictions_df["Prediction"][i]:.2f}', 
                    ha='center', color='black', fontweight='bold', fontsize=14)

        st.pyplot(fig)

        # Second Chart: Grade Progression (G1 to G3)
        st.write("### **Grade Progression (G1 to G3)**")

        # Data for progression from G1 to G2 to G3
        grades = [g1, g2, linear_predictions[0]]  # G1, G2, and predicted G3 (using linear model prediction)
        grade_labels = ['G1', 'G2', 'G3']

        # Plotting the grade progression
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.plot(grade_labels, grades, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

        # Adding labels for each point
        for i, txt in enumerate(grades):
            ax.annotate(f'{txt:.2f}', (grade_labels[i], grades[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=12, color='red')

        ax.set_title('Grade Progression (G1 to G3)', fontsize=18)
        ax.set_xlabel('Grade Stage (G1 → G2 → G3)', fontsize=14)
        ax.set_ylabel('Predicted Grade (G3)', fontsize=14)

        # Show the plot
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")