# Use an official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app_directory

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "appcode.py"]