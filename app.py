from flask import Flask, request 
from model import predict_model

app = Flask(__name__)  

@app.route('/')  # '/' = default request
def basic():
    return 'api server started'

@app.route('/soil', methods=['GET'])  # '/soil' = request # get() is used by Flask and we have to use plural form of method name
def soil():
    value = request.args.get('soil')
    print(value)
    value = float(value)
    response = predict_model(value)
    return {'msg': response}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
