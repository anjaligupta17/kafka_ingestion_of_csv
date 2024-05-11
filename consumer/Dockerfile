# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the consumer script into the container
COPY process_csv.py .

# Run process_csv.py when the container launches
CMD ["python", "process_csv.py"]
