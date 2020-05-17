function onClickedEstimateDisease() {
    var age = document.getElementById("age");
    var sex = document.getElementById('sex');
    var cp = document.getElementById('chestPain');
    var bp = document.getElementById('bloodPressure');
    var chol = document.getElementById('cholestrol');
    var sugar = document.getElementById('sugar');
    var ecg = document.getElementById('ecg');
    var heartRate = document.getElementById('heartRate');
    var angina = document.getElementById('angina');
    var oldPeak = document.getElementById('oldPeak');
    var vessels = document.getElementById('vessels');
    var thal = document.getElementById('thal');
    var output = document.getElementById('output');

    var url ='http://127.0.0.1:5000/predict_disease';
    //var url = 'E:\Project\Heart Disease Prediction\server\server\predict_disease'
    $.post(url, {
        age: parseFloat(age.value),
        sex: parseFloat(sex.value),
        cp: parseFloat(cp.value),
        bp: parseFloat(bp.value),
        chol: parseFloat(chol.value),
        sugar: parseFloat(sugar.value),
        ecg: parseFloat(ecg.value),
        heartRate: parseFloat(heartRate.value),
        angina: parseFloat(angina.value),
        oldPeak: parseFloat(oldPeak.value),
        vessels: parseFloat(vessels.value),
        thal: parseFloat(thal.value),
    },function(data, status) {
        console.log(data.estimate_disease);
        output.innerHTML = "<h2>" + data.estimate_disease.toString() + "</h2>";
        console.log(status);
    });
    console.log(age.value,sex.value,cp.value,bp.value,chol.value,sugar.value,ecg.value,heartRate.value,angina.value,oldPeak.value,vessels.value,thal.value);
}
