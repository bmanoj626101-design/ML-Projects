# raisin_app.py
import streamlit as st
import pickle
import numpy as np

# Load model
with open("VS code/cdk.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🍇 Raisin Type Classifier")

st.write("Enter raisin features to predict whether it's **Kecimen** or **Besni**.")

# Input fields
area = st.number_input("Area", min_value=0.0)
major_axis = st.number_input("MajorAxisLength", min_value=0.0)
minor_axis = st.number_input("MinorAxisLength", min_value=0.0)
eccentricity = st.number_input("Eccentricity", min_value=0.0, max_value=1.0)
convex_area = st.number_input("ConvexArea", min_value=0.0)
extent = st.number_input("Extent", min_value=0.0, max_value=1.0)
perimeter = st.number_input("Perimeter", min_value=0.0)

if st.button("Predict Raisin Type"):
    features = np.array([[area, major_axis, minor_axis,
                          eccentricity, convex_area, extent, perimeter]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Raisin Type: **{prediction}**")
