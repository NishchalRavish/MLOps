from flask import Flask,render_template,request,url_for
import numpy as np 
import pandas as pd 
import os 
import joblib 

app = Flask(__name__)

model_name = 'RF_Loan_model.joblib'
model = joblib.load(model_name)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        # Convert the data from the html form into dict for better usability
        request_data = dict(request.form)
        del request_data['First_Name']
        del request_data['Last_Name']
        request_data = {k:int(v) for k,v in request_data.items()}
        data = pd.DataFrame([request_data])
        data['TotalIncome'] = data['applicant_income'] + data['co_applicant_income']
        data['TotalIncome'] = np.log(data['TotalIncome']).copy()
        data = data[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area','TotalIncome']]
        
        prediction = model.predict(data)
        prediction_value = prediction[0]
        
        if int(prediction_value) ==1:
            result = "Congrats Approved"

        if int(prediction_value) ==0:
            result = "Sorry Rejected"
            
        return render_template('homepage.html',prediction=result)

@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Not Found"

if __name__ =="__main__":
    app.run()