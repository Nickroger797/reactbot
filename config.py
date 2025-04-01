import os

# Add environment variables or use a config file to manage sensitive data like tokens
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
LOG_CHANNEL = os.getenv("LOG_CHANNEL")
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL")
PORT = int(os.getenv("PORT", 8080))
