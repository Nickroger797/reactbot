import os

# Load environment variables
API_ID = int(os.getenv("API_ID", 0))  # Default: 0 (अगर env var ना मिले)
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))  # Default: 0
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL", 0))  # Default: 0

# Validate required variables
if not all([API_ID, API_HASH, BOT_TOKEN]):
    raise ValueError("⚠️ Error: Required environment variables are missing!")
