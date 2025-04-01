# Base image for Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app/

# Expose the port (same as in config.py)
EXPOSE 8080

# Command to run the bot
CMD ["python", "main.py"]
