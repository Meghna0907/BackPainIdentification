import numpy as np
import pandas as pd
from flask import Flask, request, render_template, redirect
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = [ "pelvic_incidence", "pelvic tilt","lumbar_lordosis_angle","sacral_slope", "pelvic_radius", "degree_spondylolisthesis",
                       " pelvic_slope", "Direct_tilt", "thoracic_slope", "cervical_tilt","sacrum_angle","scoliosis_slope"]
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
        
    if output == 1:
        res_val = "Abnormal"
    else:
        res_val = "Normal"

    return render_template('index.html', prediction_text='Patient has {} spine'.format(res_val))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

