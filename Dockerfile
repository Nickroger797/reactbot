FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set environment variables for Koyeb
ENV API_ID=${API_ID}
ENV API_HASH=${API_HASH}
ENV BOT_TOKEN=${BOT_TOKEN}
ENV LOG_CHANNEL=${LOG_CHANNEL}
ENV FORCE_SUB_CHANNEL=${FORCE_SUB_CHANNEL}
ENV MONGO_URI=${MONGO_URI}
ENV PORT=${PORT}

# Command to run the bot
CMD ["python", "main.py"]
