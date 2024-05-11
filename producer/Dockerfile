# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the producer script into the container
COPY fetch_csv.py .

# Install any needed packages specified in requirements.txt
RUN pip install requests

# Run fetch_csv.py when the container launches
CMD ["python", "fetch_csv.py"]
