import pandas as pd
import streamlit as st
import pickle
import numpy as np

#Load the model
with open('model.pkl', 'rb') as file:
    # Load the data from the file
    model = pickle.load(file)

with open('my_scalar.pkl', 'rb') as file:
    # Load the data from the file
    scalar = pickle.load(file)



#streamlit app
st.title('Medical Insurance Cost Predictor')
st.write('Enter the details to predict the medical insurance cost.')
#Input fields
age = st.number_input('Enter the age:', min_value=0, max_value=100, step=1)
sex=st.selectbox('Select the gender:',['male','female'])
smoker=st.selectbox('Select the smoker:',['yes','no'])
bmi=st.number_input('Enter the BMI:', min_value=10.0, max_value=60.0, step=0.1)
children=st.number_input('Enter the number of children:', min_value=0, max_value=5, step=1)
region=st.selectbox('Select the region:',['southwest','southeast','northwest','northeast'])

#Predict the cost
if st.button('Predict'):
    #Preprocess the input data
    input_data=pd.DataFrame({'age':[age],
                              'sex':[sex],
                              'smoker':[smoker],
                              'bmi':[bmi],
                              'children':[children],
                              'region':[region]})
    #Encode the categorical variables
    input_data['sex'] = input_data['sex'].map({'male': 1, 'female': 0})
    input_data['smoker'] = input_data['smoker'].map({'yes': 1, 'no': 0})
    input_data['region'] = input_data['region'].map({'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3})

    # Scale the numerical features
    # IMPORTANT: The list of columns and their order must exactly match what the scaler was trained on.
    # We'll assume the scaler was trained on ['age', 'bmi', 'children'].
    numerical_features = ['age', 'bmi', 'children']
    input_data[numerical_features] = scalar.transform(input_data[numerical_features])

    #Rearrange the columns to match the order used for training the model
    features=['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    input_data=input_data[features]
    # Make the prediction
    # IMPORTANT: The final column order of input_data must match the order used for training the model.
    prediction = model.predict(input_data)
    # Display the prediction
    st.success(f'The predicted medical insurance cost is: ${prediction[0]:.2f}')
