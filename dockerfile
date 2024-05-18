# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the entire contents of the src/ directory into the container at /app/src
COPY src/ /app/src

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Set environment variable to ensure Python prints to stdout/stderr without buffering
ENV PYTHONUNBUFFERED=1

# Add the src directory to the Python path
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run your main script
CMD ["python", "/app/src/main.py"]
