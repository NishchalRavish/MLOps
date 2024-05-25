import joblib
import streamlit as st
import numpy as np

model_name = 'RF_Loan_model.joblib'
model = joblib.load(model_name)

#Back End
def prediciton(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):

    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0

    if Married == "Yes":
        Married = 1
    else:
        Married = 0

    if Education == "Graduate":
        Education = 0
    else:
        Education = 1
        
    if Self_Employed == "Yes":
        Self_Employed = 1
    else:
        Self_Employed = 0

    if Credit_History == "Outstanding Loan":
        Credit_History = 1
    else:
        Credit_History = 0   
        
    if Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "Semi Urban":
        Property_Area = 1  
    else:
        Property_Area = 2  
    Total_Income =    np.log(ApplicantIncome + CoapplicantIncome)
    
    prediciton = model.predict([[Gender, Married, Dependents, Education, Self_Employed,LoanAmount, Loan_Amount_Term, Credit_History, Property_Area,Total_Income]])
    
    if prediciton==0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
        
    return pred
        



# Front End
def main():
    st.title('Loan Prediciton App')
    
    st.header('Please Enter the details correctly')
    
    Gender = st.selectbox("Gender",("Male","Female"))
    Married = st.selectbox("Married",("Yes","No"))
    Dependents = st.number_input("No of Deps")
    Education = st.selectbox("Education",("Graduate","Not Graduate"))
    Self_Employed = st.selectbox("Self_Employed",("Yes","No"))
    ApplicantIncome = st.number_input("ApplicantIncome")
    CoapplicantIncome = st.number_input("CoapplicantIncome")
    LoanAmount = st.number_input("LoanAmount")
    Loan_Amount_Term = st.number_input("LoanAmount Term")
    Credit_History = st.selectbox("Credit History",("Outstanding Loan","No Loan"))
    Property_Area = st.selectbox("Property Area",("Urban","Semi Urban","Rural"))
    
    if st.button("Predict"):
        result = prediciton(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
        
        if result =='Approved':
            st.success('Loan Approved Congrats !')
        
        else:
            st.error('Loan Not Approved')

if __name__ == "__main__":
    main()