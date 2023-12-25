import pickle
import os
import pandas as pd

'''file_path = (r'D:\Drug Classification\app\api\models\pipeline.pickle')
with open(file_path, 'rb') as f:
    loaded_pipe = pickle.load(f)
'''
# Define the base directory
base_dir = os.path.dirname(os.path.abspath(r'D:\Drug Classification\app\api\app.py'))

# Construct the file path using the base directory
file_path = os.path.join(base_dir, 'models', 'pipeline.pickle')

# Load the model
with open(file_path, 'rb') as f:
    loaded_pipe = pickle.load(f)



def predict_pipeline(loaded_pipe ,age, sex, bp, cholesterol, na_to_k):

    input_data = pd.DataFrame([[age, sex, bp, cholesterol, na_to_k]],
                              columns=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'])

    predictions = loaded_pipe.predict(input_data)

    return predictions[0]


if __name__ == "__main__":

    predictions = predict_pipeline(loaded_pipe ,age = 65, sex = 'F', bp ='High' , cholesterol = 'High', na_to_k = 10.23)
    print(predictions)