import logging
from pyrogram import Client
from handlers import start, reaction_game, ai_reactions, connect, force_sub
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, API_ID, API_HASH, MONGO_URI
from db import store_new_user  
import server  # Import server.py for fake web server (Koyeb health check)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pyrogram Client
bot = Client("reaction_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Function to log new users in MongoDB
def log_new_user(user_id, username):
    try:
        store_new_user(user_id, username)
    except Exception as e:
        logger.error(f"Failed to log user {user_id}: {e}")

# Run the bot
if __name__ == "__main__":
    logger.info("🚀 Bot is starting...")
    server.start_server()  # Start the fake web server (for Koyeb health check)
    bot.run()
