# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the requirements and install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Default command
CMD ["python", "app.py"]
