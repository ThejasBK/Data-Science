from flask import Flask, request, jsonify
import utils
app = Flask(__name__)

@app.route("/predict_disease",methods=['GET','POST'])
def predict_disease():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp = int(request.form['cp'])
    bp = int(request.form['bp'])
    chol = int(request.form['chol'])
    sugar = int(request.form['sugar'])
    ecg = int(request.form['ecg'])
    heartRate = int(request.form['heartRate'])
    angina = int(request.form['angina'])
    oldPeak = float(request.form['oldPeak'])
    vessels = int(request.form['vessels'])
    thal = int(request.form['thal'])

    response = jsonify({
        'estimate_disease': utils.predict_disease(age,sex,cp,bp,chol,sugar,ecg,heartRate,angina,oldPeak,vessels,thal)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    utils.load_saved_artifacts()
    app.run()