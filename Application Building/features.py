from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')
from features import FeatureExtraction

app = Flask(__name__)

xgb = pickle.load(open("XGBoostClassifier.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        url = request.form["url"]
        obj = FeatureExtraction(url)

        x = np.array(obj.getFeaturesList()).reshape(1,13)
        print(x)
        y_pred =xgb.predict(x)[0]
        print(y_pred)
        y_pro_phishing = xgb.predict_proba(x)[0,0]
        print(y_pro_phishing)
        y_pro_non_phishing = xgb.predict_proba(x)[0,1]
        print(y_pro_non_phishing)

        if(y_pro_phishing*100<60):
            msg="Treat! They say, 'Not all those who wander are lost'. And you are definitely not lost. Have a safe day exploring!!"
            flag=1
        else:
            msg="Trick! They say, 'Not all those who wander are lost'. But you are definitely lost. Find other sites to explore!!"
            flag=-1

        return render_template('result.html', msg=msg, url=url, val=flag)

    return render_template("index.html")

@app.route("/report")
def report():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)