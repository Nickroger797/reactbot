# Use official Python image (slim for smaller size)
FROM python:3.9-slim  

# Set the working directory
WORKDIR /app

# Install system dependencies (optional, if needed)
RUN apt-get update && apt-get install -y gcc

# Copy requirements file first (for caching layers)
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the default command to run the bot
CMD ["python3", "main.py"]
