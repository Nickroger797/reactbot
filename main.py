import asyncio
import logging
from pyrogram import Client, filters
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, API_ID, API_HASH
from db import store_new_user  
import server  # Fake server for Koyeb

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pyrogram Client
bot = Client("reaction_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ Start Command Handler
@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Hello! I'm a Reaction Bot. Use commands to interact!")

# ✅ Other Command Handlers (अगर और कमांड हैं तो यहां जोड़ो)
@bot.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text("ℹ️ Available Commands:\n/start - Start the bot\n/help - Show this help message")

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

    # Start the fake web server (for Koyeb health check)
    await server.start_server()

    # Keep the bot running
    await asyncio.Event().wait()  # Infinite loop to keep running

# Run the bot using asyncio.run
if __name__ == "__main__":
    asyncio.run(main())
