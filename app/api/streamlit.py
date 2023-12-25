import streamlit as st
import pandas as pd
import pickle

# Load the model from the pickle file
with open(r'D:\Drug Classification\app\api\models\pipeline.pickle', 'rb') as file:
    model = pickle.load(file)


# Set up the Streamlit app
def main():
    st.title('Drug Classification Model')

    # Create input fields for the model features
    age = st.number_input('Age', min_value=0, max_value=120)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    bp = st.selectbox('BP', ['Low', 'Normal', 'High'])
    cholesterol = st.selectbox('Cholesterol', ['Normal', 'High'])
    na_to_k = st.number_input('Na to K Ratio', min_value=0.0, max_value=50.0)

    # Prediction button
    if st.button('Predict'):
        # Prepare the input data for the model
        input_data = pd.DataFrame([[age, sex, bp, cholesterol, na_to_k]],
                                  columns=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'])

        # Make the prediction
        prediction = model.predict(input_data)
        st.write(f'Predicted Drug: {prediction[0]}')


if __name__ == '__main__':
    main()
