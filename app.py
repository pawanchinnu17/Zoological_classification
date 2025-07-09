import streamlit as st
import joblib
import numpy as np

# Load the trained XGBoost model (make sure it's saved as xgboost_model.pkl)
model = joblib.load('XGBoost_model.pkl')

# Title and description
st.title(" Classification of Zoological Species Using Machine Learning")
st.markdown("Enter the features of the animal below and click **Predict** to classify it using a trained XGBoost model.")

# Input fields for all 16 features
hair = st.selectbox("Hair", [0, 1])
feathers = st.selectbox("Feathers", [0, 1])
eggs = st.selectbox("Lays Eggs", [0, 1])
milk = st.selectbox("Produces Milk", [0, 1])
airborne = st.selectbox("Airborne", [0, 1])
aquatic = st.selectbox("Aquatic", [0, 1])
predator = st.selectbox("Predator", [0, 1])
toothed = st.selectbox("Toothed", [0, 1])
backbone = st.selectbox("Has Backbone", [0, 1])
breathes = st.selectbox("Breathes", [0, 1])
venomous = st.selectbox("Venomous", [0, 1])
fins = st.selectbox("Has Fins", [0, 1])
legs = st.number_input("Number of Legs", min_value=0, max_value=8, step=1)
tail = st.selectbox("Has Tail", [0, 1])
domestic = st.selectbox("Domestic", [0, 1])
catsize = st.selectbox("Cat-Sized", [0, 1])

# Predict on button click
if st.button("Predict"):
    # Arrange features in the correct order
    features = np.array([[hair, feathers, eggs, milk, airborne, aquatic,
                          predator, toothed, backbone, breathes, venomous,
                          fins, legs, tail, domestic, catsize]])
    
    # Predict using XGBoost model (classes start from 0)
    prediction_zero_based = model.predict(features)[0]
    
    # Shift back to original class numbers (1 to 7)
    prediction = prediction_zero_based + 1

    # Class label mapping
    class_dict = {
        1: "🐶 Mammal",
        2: "🦅 Bird",
        3: "🦎 Reptile",
        4: "🐟 Fish",
        5: "🐸 Amphibian",
        6: "🪲 Bug",
        7: "🕷️ Invertebrate"
    }

    st.success(f"Predicted Class: **{prediction} - {class_dict.get(prediction, 'Unknown')}**")
