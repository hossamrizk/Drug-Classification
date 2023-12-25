from flask import Flask, jsonify, request
from utilities import predict_pipeline,loaded_pipe

app = Flask(__name__)

@app.post('/predict')
def predict():
    # Extracting data from the POST request
    data = request.json  # Assuming the data is sent in JSON format

    # Extracting required features
    age = data.get('Age')
    sex = data.get('Sex')
    bp = data.get('BP')
    cholesterol = data.get('Cholesterol')
    na_to_k = data.get('Na_to_K')

    # Calling the predict_pipeline function with the extracted features
    predictions = predict_pipeline(loaded_pipe,age=age, sex=sex, bp=bp, cholesterol=cholesterol, na_to_k=na_to_k)

    # Return the predictions as a JSON response
    return jsonify({'Drug category is': predictions})

if __name__ == '__main__':
    app.run(debug=True)