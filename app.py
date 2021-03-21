# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:32:01 2021

@author: karthik
"""
from flask import Flask,request,render_template
import joblib
import numpy as np

app=Flask(__name__)
model=joblib.load("updated_model.sav")
def func(var):
    dict_val={"private":0,"self emp":0,"govt job":0,"children":0,"never worked":0}
    dict_val[var]=1
    return dict_val
def smoke(var):
    dict_val={"never smoked":0,"smoked":0,"formerly smoked":0,"unknown":0}
    dict_val[var]=1
    return dict_val
@app.route('/')
def home():
    return render_template("Index.html")
@app.route("/predict", methods = ["GET", "POST"])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == "POST":
        
        gender=int(request.form["Gender"])
        age=float(request.form["Age"])
        hypertension=int(request.form["Hypertension"])
        heart_disease=int(request.form["Heart disease"])
        married=int(request.form["Ever Married"])
        dictionary=func(request.form["worktype"])
        private=int(dictionary["private"])
        self_emp=int(dictionary["self emp"])
        govt_job=int(dictionary["govt job"])
        children=int(dictionary["children"])
        never_worked=int(dictionary["never worked"])
        Residence_type_urban=int(request.form["Residence type"])
        avg_g_l=float(request.form["average glucose level"])
        bmi=float(request.form["bmi"])
        dict2=smoke(request.form["smoke"])
        never_smoked=int(dict2["never smoked"])
        smoked=int(dict2["smoked"])
        for_sm=int(dict2["formerly smoked"])
        unknown=int(dict2["unknown"])
        data_array=([[age,hypertension,heart_disease,avg_g_l,bmi,gender,married,
                never_worked,private,self_emp,children,Residence_type_urban,
                for_sm,never_smoked,smoked]])
        
        pred=model.predict(data_array)
        if int(pred)==1:
            output="Risk is high , high chance of getting heartstroke"
        elif int(pred)==0:
            output="Chill,You are safe"
            
        return render_template("Index.html",prediction_text=output) 
    return render_template('Index.html')


if __name__=='__main__':
    app.run(debug=True)    
#model.predict([[69.0,0,0,94.39,22.800000,0,0,0,1,0,0,1,0,1,0]])
#pred