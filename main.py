import asyncio
import logging
from pyrogram import Client, idle
from handlers import start, reaction_game, ai_reactions, connect, force_sub
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, API_ID, API_HASH
from db import store_new_user  # Import MongoDB function

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

# Bot main function
async def main():
    logger.info("🚀 Bot is starting...")
    await bot.start()
    logger.info("✅ Bot started successfully!")
    await idle()  # Keeps the bot running
    await bot.stop()  # Stops the bot gracefully

# Run the bot using asyncio.run (Best practice)
if __name__ == "__main__":
    asyncio.run(main())
