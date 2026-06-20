# Step 1: Use an official minimal Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy your project files into the container's /app folder
COPY dashboard.py .
COPY config.json .

# Step 4: Install the required libraries directly inside the container
RUN pip install requests

# Step 5: Tell the container exactly what command to run when it boots up
CMD ["python", "dashboard.py"]