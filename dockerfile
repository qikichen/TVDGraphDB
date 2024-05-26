# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire contents of the src/ and tests/ directory into the container at /app/src and /app/tests respectively
COPY src/ src/
COPY tests/ tests/

# Set environment variable to ensure Python prints to stdout/stderr without buffering
ENV PYTHONUNBUFFERED=1

# Add the src directory to the Python path
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Run your main script
CMD ["python", "/app/src/main.py"]