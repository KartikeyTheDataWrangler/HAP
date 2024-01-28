from flask import Flask, request, render_template, redirect,session
from src.hap.utils import read_object, save_object
from src.hap.logger import logging
from src.hap.exception import CustomException
from src.hap.config.configeration import Configuration_Creator
import numpy as np

logging.info("Flask app started")
app = Flask(__name__)
app.secret_key = 'BELETH'
preprocessor_dir = Configuration_Creator().create_preprocessor()
@app.route("/", methods=["GET", "POST"])
def home_html():
    if request.method == "POST":
        mydict = request.form
        age = mydict['age']
        sex = mydict['sex']
        diet = mydict['diet']
        bmi = mydict['cat_bmi']
        triglycerides = mydict['cat_Triglycerides']
        continent = mydict['continent']
        pulsepressure = mydict['cat_pulse']
        diabetes = mydict['cat_diabetes']
        cholestrol = int(176)
        family_history = mydict['rem_family_history']
        alchohol_consumption = mydict['rem_Alch_Consumption']
        heart_problems = mydict['rem_heartproblems']
        medication = mydict['rem_medication']
        stress = mydict['rem_stress']
        physical_activity = mydict['rem_physical']
        sleep = mydict['rem_sleephrs']
        
        logging.info("data collected and made into an array")  
        data = np.array([age, sex, diet, bmi, triglycerides, continent,pulsepressure,diabetes,
                cholestrol,family_history,alchohol_consumption,heart_problems,medication,
                stress,physical_activity,sleep]).reshape(1,-1)
        
        
        logging.info(data)
        rf_model = read_object(preprocessor_dir + "/bestmodel")
        predict = rf_model.predict(data)
        logging.info(predict)
        
        key = str(predict)
        
        #mapping result
        result_mapper = {"[0]":"patient has no risk of heart attack",
                         "[1]":"patient is predicted to have a risk of heart attack"}
        
        #print(result_mapper[key])
        
        session['result'] = result_mapper[key]
        
        return redirect("/prediction")
    else:
        return render_template('home.html')  

@app.route('/prediction',methods=["GET"])
def show_prediction():
    result = session.get('result')
    print(result)
    logging.info("inside predict html")
    return render_template("predict.html",prediction=result)      
        
        
        
        
if __name__=="__main__":
    
    app.run(host="0.0.0.0",debug=True) 
    