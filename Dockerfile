# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables (optional if not already set in Koyeb)
ENV API_ID=your_api_id
ENV API_HASH=your_api_hash
ENV BOT_TOKEN=your_bot_token
ENV MONGO_URI=your_mongo_uri
ENV LOG_CHANNEL=your_log_channel
ENV FORCE_SUB_CHANNEL=your_force_sub_channel

# Expose the port
EXPOSE 8080

# Run the bot
CMD ["python", "main.py"]
