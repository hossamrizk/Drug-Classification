FROM python:3.8

# Copying requirements.txt first to leverage Docker caching
COPY requirements.txt /app/api/requirements.txt

WORKDIR /app/api

RUN pip install -r requirements.txt

# Copy the entire API directory into the container
COPY . .

# Copy the pipeline.pickle file into the appropriate directory in the container
COPY models/pipeline.pickle /app/api/models/pipeline.pickle

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
