# Base image for Raspberry Pi compatibility and Python installed
FROM balenalib/raspberry-pi-python:3.7-buster

# Install dependencies and picamera library
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-picamera \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the script into the container
COPY capture_image.py .

# Command to execute when the container starts
CMD ["python", "./capture_image.py"]
