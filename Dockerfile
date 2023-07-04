# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code to the container
COPY server.py .

# Expose the desired port (e.g., 5000)
EXPOSE 5000

# Set the command to run the server
CMD ["python", "server.py"]
