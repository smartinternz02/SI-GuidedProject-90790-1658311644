# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:39:41 2020

@author: DELL
"""

from flask import Flask, render_template, request# Flask-It is our framework which we are going to use to run/serve our application.
#request-for accessing file which was uploaded by the user on our application.

import numpy as np #used for numerical analysis

import pickle

model = pickle.load(open("cardiac_arrest_model.pkl", "rb"))
app = Flask(__name__) #our flask app


@app.route('/') #default route
def hello_world():
  return render_template("index.html")
  
@app.route('/login', methods = ['POST']) #Main page route
def admin():

  q = request.form['age']
  r = 1 if request.form['anaemia'] == "yes" else 0
  s = request.form['cpl']
  t = 1 if request.form['diabetes'] == "yes" else 0
  u = request.form['efl']
  v = request.form['hbpl']
  p = request.form['p']
  w = request.form['scl']
  x = request.form['ss']
  y = 1 if request.form['gender'] == "male" else 0
  z = 1 if request.form['smoking'] == "yes" else 0

  sample = [[q, r, s, t, u, v, p, w, x, y, z]]

  test = model.predict(sample)

  if test == 0:
    test = "The Risk of Cardiac Arrest is Low. "
  elif test == 1:
    test = "The Risk of Cardiac Arrest is High. "

  return render_template("index.html", test = test)


# age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,
# high_blood_pressure,platelets,serum_creatinine,serum_sodium,
# sex,smoking,time,DEATH_EVENT


@app.route('/user')
def user():
  return "Hye User"



if __name__ == '__main__':
  #app.run(host='0.0.0.0', port=8000,debug=False)
  app.run(debug = True) #running our flask app