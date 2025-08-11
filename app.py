import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('logistic_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🚢 Titanic Survival Prediction App")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 600.0, 50.0)
embarked = st.selectbox("Embarked", ["S", "C", "Q"])

# Label encoding
sex_encoded = 1 if sex == "female" else 0
embarked_map = {"S": 2, "C": 0, "Q": 1}
embarked_encoded = embarked_map[embarked]

input_data = np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("🎉 Passenger would have SURVIVED.")
    else:
        st.error("💀 Passenger would NOT have survived.")
