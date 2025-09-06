import streamlit as st
import joblib
import pandas as pd

#load model
model = joblib.load('loan_eligibility_model1.pkl')

st.title('Loan prediciton app')

#take users input 
person_gender = st.radio('Select your gender:',
                            ('male','female'))
st.write('you selected :',person_gender)

person_education = st.radio('Select your education:',
                            ('Masters','Bachelor','High School','Associate', 'Doctorate'))
st.write('you selected: ',person_education)

person_emp_exp = st.number_input('Your work experience',min_value=0)

person_home_ownership = st.radio('how do you live',
                                 ('OWN','RENT','MORTAGE','OTHER'))
st.write('Type of living is:', person_home_ownership)

loan_intent = st.selectbox(
    "what is your loan intent",
    ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT','DEBTCONSOLIDATION']
)

loan_int_rate = st.number_input('Enter loan interset rate',min_value=2.0,step=0.1)

cb_person_cred_hist_length = st.number_input('What is your credit lenth:',min_value=0)

previous_loan_defaults_on_file = st.radio('Do the candidate have pervious default loan:',
                                          ('Yes','NO'))

person_income = st.number_input('Income',min_value=0)

person_age = st.number_input('Age',min_value=18,max_value=90)

loan_amnt = st.number_input('Amount',min_value=100)

loan_percent_income = st.number_input('Loan percent income',min_value=0.0,step=0.1)

credit_score = st.number_input('Score',min_value=0)


if st.button('Predict'):
    input_data = pd.DataFrame([[person_age,person_gender,person_education,person_income,person_emp_exp,
                                person_home_ownership,loan_amnt,loan_intent,loan_int_rate,loan_percent_income,
                                cb_person_cred_hist_length,credit_score,previous_loan_defaults_on_file]],
                              columns=['person_age','person_gender','person_education','person_income','person_emp_exp',
                                       'person_home_ownership','loan_amnt','loan_intent','loan_int_rate','loan_percent_income',
                                       'cb_person_cred_hist_length','credit_score','previous_loan_defaults_on_file'])
    
    prediction = model.predict(input_data)[0]
    st.write('Eligible for loan' if prediction==1 else 'Not eligible')