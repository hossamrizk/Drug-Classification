# Drug Classification Project

This project is geared towards classifying drug types based on specific parameters such as age, sex, blood pressure, cholesterol, and the Na_to_K ratio. It employs various technologies and tools for model building, data visualization, API development, containerization, and testing.

## Technologies Used

### Model Development
- **Scikit-learn (sklearn):** Utilized for building the classification model.

### Exploratory Data Analysis (EDA)
- **Plotly:** Employed for visualizing and exploring the dataset.

### API Development
- **Flask:** Used to create an API for seamless interaction with the model.

### Containerization
- **Docker:** Employed for containerizing the entire project.

### Testing
- **Postman:** Testing was conducted using Postman's website to ensure the API's functionality.

### Additional API Implementation
- **Streamlit:** Developed an additional API without Docker, which performed effectively.

## Project Workflow

1. **Data Collection and Preprocessing:** Acquired and processed data containing information on age, sex, blood pressure, cholesterol, and Na_to_K ratio.
  
2. **Model Building:** Utilized Scikit-learn to construct a classification model based on the collected data.
  
3. **Exploratory Data Analysis:** Employed Plotly for in-depth visualization and exploration of the dataset to derive insights.

4. **API Development:** Implemented Flask to create an API, allowing seamless interaction with the classification model.

5. **Containerization:** Leveraged Docker to encapsulate the entire project, ensuring easy deployment and consistency across different environments.

6. **Testing:** Conducted comprehensive testing using Postman's website to validate the API's functionality and performance.

7. **Additional API Implementation:** Developed an alternate API using Streamlit, providing an alternative interface without Docker, which proved to work efficiently.

## Try it Yourself!

Experience the ease of running this project without the hassle of downloading multiple files and dependencies by leveraging the power of Docker.

### Docker Installation

If you haven't installed Docker yet, ensure it's installed on your system by following the [official Docker installation guide](https://docs.docker.com/get-docker/).

### Running with Docker

Execute the following commands in your terminal:

1. Pull the Docker image:

    ```bash
    docker pull hossamrizk/drugclassification
    ```

2. Launch the server:

    ```bash
    docker run -p 5000:5000 hossamrizk/drugclassification
    ```

Once the process completes, navigate to Postman's website to test the API.

### Alternative: Running without Docker

If Docker isn't your preference, easily run the project without additional dependencies:

1. In your IDE terminal, execute:

    ```bash
    streamlit run streamlit.py
    ```

This command will initiate the application without the need for Docker, providing a streamlined experience for direct usage.



