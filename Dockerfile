FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all the files
COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV BOT_TOKEN=your-bot-token-here
ENV API_ID=your-api-id-here
ENV API_HASH=your-api-hash-here
ENV MONGO_URI=your-mongo-uri-here
ENV LOG_CHANNEL=your-log-channel-id
ENV FORCE_SUB_CHANNEL=your-force-sub-channel-id
ENV PORT=8080

# Run the bot
CMD ["bash", "start.sh"]
