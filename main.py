import asyncio
import logging
import os
from pyrogram import Client, filters
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, API_ID, API_HASH
from db import store_new_user
import server  # Fake server for Koyeb

# ✅ Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Pyrogram Client with MongoDB Session (Fixed)
SESSION_STRING = os.getenv("SESSION_STRING")  # Fetch session from environment

bot = Client(
    name="reaction_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=SESSION_STRING if SESSION_STRING else None  # Use session if available
)

# ✅ Start Command Handler
@bot.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or "Unknown"

    # Log new user to MongoDB
    log_new_user(user_id, username)

    await message.reply_text("👋 Hello! I'm a Reaction Bot. Use commands to interact!")

# ✅ Help Command Handler
@bot.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text("ℹ️ Available Commands:\n/start - Start the bot\n/help - Show this help message")

# ✅ Function to log new users in MongoDB
def log_new_user(user_id, username):
    try:
        store_new_user(user_id, username)
        logger.info(f"✅ New user added: {user_id} ({username})")
    except Exception as e:
        logger.error(f"❌ Failed to log user {user_id}: {e}")

# ✅ Bot main function
async def main():
    logger.info("🚀 Bot is starting...")
    await bot.start()
    logger.info("✅ Bot started successfully!")

    # ✅ Start the fake web server (for Koyeb health check)
    await server.start_server()

    # ✅ Keep the bot running
    await asyncio.Event().wait()

# ✅ Run the bot using asyncio.run
if __name__ == "__main__":
    asyncio.run(main())
