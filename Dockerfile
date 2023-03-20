# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip --timeout=999 install -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
