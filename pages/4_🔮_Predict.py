import streamlit as st
import pandas as pd
import numpy as np
import joblib  
import os
from sklearn.preprocessing import LabelEncoder
from catboost import CatBoostClassifier
from imblearn.over_sampling import RandomOverSampler
from  PIL import Image

st.set_page_config(
    page_icon= "🔮",
    page_title= "Predict",
    layout = "wide"
    )

st.title(f"**Predict Customer Churn ➡️**")
st.write(
    """
    Keep your customers happy!  This app helps you predict customer churn using machine learning, empowering you to take proactive steps and prevent revenue loss.
    """
     )
#image
chun_img = Image.open(
    os.path.join (
        os.getcwd(),
        "assets/images/chun customer image 2.png"
        )
    )

#display img
st.image(
    chun_img,
    use_column_width=True,
    caption= " Customers leaving can sting your business. Predict & prevent churn!"
    )

# Initialize session state
if 'final_prediction' not in st.session_state:
    st.session_state.final_prediction = None

# Load models and cache them
@st.cache(allow_output_mutation=True)
def load_catboost():
    Catboost = joblib.load('models/catboost_pipeline.joblib')
    return Catboost

@st.cache(allow_output_mutation=True)
def load_logistic():
    Logistic = joblib.load('models/logistic_pipeline.joblib')
    return Logistic

# Create a display form function
def user_input_form():
    with st.form(key='user_input_form'):
        customerID = st.text_input(label='CustomerID')
        tenure = st.number_input(label='tenure')
        MonthlyCharges = st.number_input(label='MonthlyCharges')
        TotalCharges = st.number_input(label='TotalCharges')
        SeniorCitizen = st.number_input(label='SeniorCitizen')
        gender = st.selectbox(label='Gender', options=['Male', 'Female'])
        Partner = st.selectbox(label='Partner', options=['Yes', 'No'])
        Dependents = st.selectbox(label='Dependents', options=['Yes', 'No'])
        PhoneService = st.selectbox(label='PhoneService', options=['Yes', 'No'])
        MultipleLines = st.selectbox(label='MultipleLines', options=['Yes', 'No'])
        InternetService = st.selectbox(label='InternetService', options=['DSL', 'Fiber Optic', 'No'])
        OnlineSecurity = st.selectbox(label='OnlineSecurity', options=['Yes', 'No', 'No Internet'])
        OnlineBackup = st.selectbox(label='OnlineBackup', options=['Yes', 'No', 'No Internet'])
        DeviceProtection = st.selectbox(label='DeviceProtection', options=['Yes', 'No', 'No Internet'])
        TechSupport = st.selectbox(label='TechSupport', options=['Yes', 'No', 'No Internet'])
        StreamingTV = st.selectbox(label='StreamingTV', options=['Yes', 'No', 'No Internet'])
        StreamingMovies = st.selectbox(label='StreamingMovies', options=['Yes', 'No', 'No Internet'])
        contract = st.selectbox(label='contract', options=['Month-to-Month', 'One year', 'Two year'])
        PaperlessBilling = st.selectbox(label='PaperlessBilling', options=['Yes', 'No'])
        PaymentMethod = st.selectbox(label='MultipleLines', options=['Electronic check', 'mailed check', 'Bank transfer(automatic)', 'Credit card(automatic)'])
        submit_button = st.form_submit_button(label='Submit')
    return 'gender', 'Partner','customerID', 'Dependents', 'tenure','PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity','OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV','StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', submit_button

def log1p_transform(X):
    X['TotalCharges'] = np.log1p(X['TotalCharges'])
    return X

# Create a select_model function
def select_model(gender,Partner,customerID,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies, Contract,PaperlessBilling, PaymentMethod):
    if st.session_state.selected_model == 'Catboost':
        pipeline = load_catboost()
        encoder = LabelEncoder()
        encoder.fit(pipeline.classes_)
    elif st.session_state.selected_model == 'Logistic':
        pipeline = load_logistic()
        encoder = LabelEncoder()
        encoder.fit(pipeline.classes_)
    else:
        pipeline = None
        encoder = None
    return pipeline, encoder

# Create a make_prediction function
def make_prediction(gender,Partner,customerID,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies, Contract,PaperlessBilling, PaymentMethod, pipeline, encoder):
    if pipeline is not None:
        data = [[gender,Partner,customerID,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies, Contract,PaperlessBilling, PaymentMethod]]
        df = pd.DataFrame(data)
        prediction = pipeline.predict(df)[0]
        probability = pipeline.predict_proba(df)[0][prediction]
        prediction = encoder.inverse_transform([prediction])[0]
        st.session_state.final_prediction = prediction
        st.session_state.final_probability = probability

# Display the form and make prediction
def main():
    gender,Partner,customerID,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies, Contract,PaperlessBilling, PaymentMethod, submit_button = user_input_form()
    if submit_button:
       st.session_state.selected_model = st.selectbox(label='Select Model', options=['Catboost', 'Logistic'])
       pipeline, encoder = select_model(gender,Partner,customerID,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies, Contract,PaperlessBilling, PaymentMethod)
       make_prediction(gender,Partner,customerID,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies, Contract,PaperlessBilling, PaymentMethod, pipeline, encoder)

# Show prediction and probability
if st.session_state.final_prediction is not None:
    st.write(f'Prediction: {st.session_state.final_prediction}')
    st.write(f'Probability: {st.session_state.final_probability}')

if __name__ == "__main__":
    main()

