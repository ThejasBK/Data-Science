import pickle
import json
import numpy as np

__model = None
__data_columns = None

def predict_disease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,ca,thal):    
    x1 = np.zeros(len(__data_columns))
    x1[0] = age
    x1[1] = sex
    x1[2] = cp
    x1[3] = trestbps
    x1[4] = chol
    x1[5] = fbs
    x1[6] = restecg
    x1[7] = thalach
    x1[8] = exang
    x1[9] = oldpeak
    x1[10] = ca
    x1[11] = thal
    return __model.predict([x1])[0]

def load_saved_artifacts():
    global  __data_columns
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/heart_disease_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(predict_disease(44,1,2,125,270,0,0,158,1,0.6,1,1))