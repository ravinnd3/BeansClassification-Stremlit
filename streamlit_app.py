import streamlit as st
import numpy as np
import pickle

st.image("bean.webp")

# Load saved models
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('PCA.pkl', 'rb') as f:
    pca = pickle.load(f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define feature inputs
columns = ['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength',
           'AspectRation', 'Eccentricity', 'ConvexArea', 'EquivDiameter',
           'Extent', 'Solidity', 'roundness', 'Compactness',
           'ShapeFactor1', 'ShapeFactor2', 'ShapeFactor3', 'ShapeFactor4']

# Class mapping
label_map = {
    0: 'BARBUNYA',
    1: 'BOMBAY',
    2: 'CALI',
    3: 'DERMASON',
    4: 'HOROZ',
    5: 'SEKER',
    6: 'SIRA'
}

st.title("Bean class classification")
st.markdown("Enter Avaiable Bean Information to Predict Classification")

# Collect user input
user_input = []
for col in columns:
    val = st.number_input(f"{col}", min_value=0.0, step=0.01)
    user_input.append(val)

# Predict button
if st.button("Classify Bean"):
    input_array = np.array(user_input).reshape(1, -1)
    scaled = scaler.transform(input_array)
    reduced = pca.transform(scaled)
    predicted_label = model.predict(reduced)[0]
    predicted_class = label_map.get(predicted_label, "Unknown")

    st.success(f"Predicted Bean Category: **{predicted_class}**")
