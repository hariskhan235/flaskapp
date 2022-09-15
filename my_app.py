# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 01:30:14 2022

@author: Haris Romeo
"""

from flask import Flask, request, jsonify
import pickle
import os

filename = 'C:/Users/Haris Romeo/Desktop/fyp_app/decisionTree.pkl'

with open(filename, 'rb') as file:
    model = pickle.load(file)
    print("model Loaded....")

app = Flask(__name__)

@app.route('/flutter', methods=['GET', 'POST'])
def f1():
    if request.method == 'POST':
        print(request.form)
    return jsonify({"hello": True})


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        request_json = request.json
        print(request_json)
        to_predict_list = request.form.to_dict()

        to_predict_list = [float(request_json['gender']),
                           float(request_json['major_subject_ssc']),
                           float(request_json['major_subject_hssc']),
                           float(request_json['interested_subject']),
                           float(request_json['ssc_percentage']),
                           float(request_json['hssc_percentage']),
                           float(request_json['family_income'])
                           ]
        print(request.form)


        # result = model.predict([[0,1,2,1,1,2,1]])
        result = model.predict([to_predict_list])
        print(result)

        if result[0] == 'CS':
            prediction = 'Bachelors Of Computer Science'

        elif result[0] == 'BBA':
            prediction = 'Bachelors of Business Administration (BBA)'
        elif result[0] == 'Engineering':
            prediction = 'Engineering Field'
        elif result[0] == 'HealthSciences':
            prediction = 'Health Sciences Field'
        elif result[0] == 'BSPhysics':
            prediction = 'Bachelors of Physics'
        elif result[0] == 'BSMaths':
            prediction = 'Bachelors of Mathematics'
        elif result[0] == 'BSEnglish':
            prediction = 'Bachelors of English'
        elif result[0] == 'Medical-Bioinformatics':
            prediction = 'Health Sciences Related Fields'
        elif result[0] == 'HealthSciences-MBBS':
            prediction = 'Health Sciences Related Field'
        elif result[0] == 'BSPsychology':
            prediction = 'Bachelors of Psychology'
        elif result[0] == 'BSBiology':
            prediction = 'Bachelors of Biology'
        elif result[0] == 'BSIslamiyat':
            prediction = 'Bachelors of Islamiat'
        elif result[0] == 'BSBotony/Zology':
            prediction = 'Bachelors in Botny / Zoology'
        elif result[0] == 'BSUrdu':
            prediction = 'Bachelors of Urdu'
        else:
            prediction = 'Something Went Wrong Please Try Again...'

        r = {"result": prediction}
        print(r)
        return jsonify(r)


@app.route('/')
def index():
    result = model.predict([[0, 1, 2, 3, 3, 3, 1]])
    print(result)

    if result[0] == 'BBA':
        prediction = 'Bachelors of business administration (BBA)'
    else:
        prediction = 'Some Thing Else'
    return prediction


@app.route('/name')
def myName():
    return "Haris Akhtar"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
