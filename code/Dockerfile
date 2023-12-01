# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container's /app directory
COPY . /app

# Install Python (if not present in the base image)
RUN apt-get update && apt-get install -y python3

# Define the command to run the Python file named sparrow.py
CMD ["python3", "sparrow.py", "0.0.0.0", "443"]
