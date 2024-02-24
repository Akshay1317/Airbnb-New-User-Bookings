import pickle
import flask

from flask import Flask, request

app = Flask(__name__)

model_pickle = open("classifier.pkl", "rb")
clf = pickle.load(model_pickle)


@app.route("/ping", methods=["GET"])
def ping():
    return "Pinging the model successful!!!"


# Creating endpoint of machine learning prediction model.
@app.route("/predict", methods=["POST"])
def prediction():
    
    # We would ask the user for few field values based on which we will give the prediction.
    # The data is mostly sent in JSON format from the client.
    req = request.get_json() # We can read what the user has sent from the body

    
    return {"country_destination": 'abc'}
