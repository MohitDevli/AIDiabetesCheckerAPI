from joblib import load
from flask import Flask, request,redirect, url_for, flash, jsonify
import numpy as np
import json


app= Flask(__name__)



@app.route('/api/', methods= ['POST'])
def makecalc():
	data = request.get_json()
	prediction = np.array2string(model.predict(data))
	return jsonify(prediction)


if __name__=="__main__":
	model= load('model/Diabetes.joblib')
	
	app.run(debug=True, host='0.0.0.0')






