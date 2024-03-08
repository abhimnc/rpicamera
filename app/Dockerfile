# Use a Balena base image for Raspberry Pi compatible with libcamera
FROM balenalib/raspberry-pi-debian-python

ENV UDEV=on

# Install kmod and any other dependencies
RUN apt-get update && apt-get install -y kmod && \
    # Clean up package lists to reduce image size
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install dependencies for libcamera
RUN install_packages libcamera-apps

RUN install_packages \
    libcamera-dev \
    libcamera-apps-lite \
    python3 \
    v4l-utils

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY capture_image.py .

# # Command to run the Python script
# CMD ["python", "./capture_image.py"]
# Copy a script that includes the modprobe command and starts your application
COPY start.sh /start.sh

# Ensure the script is executable
RUN chmod +x /start.sh

# Use the script as the entry point or command
CMD ["/start.sh"]
