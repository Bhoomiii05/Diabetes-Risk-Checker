from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(request.form[x]) for x in request.form]
    prediction = model.predict([features])[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
