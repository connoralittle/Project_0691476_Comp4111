from flask import Flask, render_template, request
import pickle
import numpy as np
import sqlite3

app = Flask(__name__)

model = pickle.load(open("diabetes_predictor.pkl", "rb"))

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/aboutme")
def aboutme_page():
    return render_template("about.html")
    
@app.route("/predict")
def predict_page():
    return render_template("predict.html")

@app.route("/result", methods=["POST"])
def predict():
    first_name = request.form["firstInput"]
    last_name = request.form["lastInput"]
    pregnancies = float(request.form["pregnancyInput"])
    glucose = float(request.form["glucoseInput"])
    blood_pressure = float(request.form["bpInput"])
    skin_thickness = float(request.form["stInput"])
    insulin = float(request.form["insulinInput"])
    bmi = float(request.form["bmiInput"])
    diabetes_pedigree = float(request.form["dpInput"])
    age = float(request.form["ageInput"])

    prediction = model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    
    connection = get_db_connection()
    sql = ''' INSERT INTO records(first_name, last_name, pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree,age,outcome)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    record = (first_name, last_name, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age, float(prediction))
    
    cur = connection.cursor()
    cur.execute(sql, record)
    connection.commit()
    connection.close()

    if prediction == 0:
        return render_template("resultNegative.html", prediction=prediction)
    else:
        return render_template("resultPositive.html", prediction=prediction)

#sql stuff
def get_db_connection():
    connection = sqlite3.connect('pima_indians_database.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/database")
def database_page():
    connection = get_db_connection()
    records = connection.execute("SELECT * FROM records").fetchall()
    connection.close()
    return render_template("database.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)