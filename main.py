import asyncio
import logging
import os
from pyrogram import Client, filters
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, API_ID, API_HASH
from db import store_new_user
import server  # Fake server for Koyeb

# ✅ Logging setup (DEBUG mode)
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG Mode enabled
    format="%(asctime)s - [%(levelname)s] - %(message)s",
)
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
    try:
        user_id = message.from_user.id
        username = message.from_user.username or "Unknown"

        # Log new user to MongoDB
        log_new_user(user_id, username)

        await message.reply_text("👋 Hello! I'm a Reaction Bot. Use commands to interact!")
        logger.info(f"✅ Sent start message to {user_id} ({username})")

    except Exception as e:
        logger.error(f"❌ Error in /start command: {e}", exc_info=True)
        await message.reply_text("⚠️ An error occurred! Check logs for details.")

# ✅ Help Command Handler
@bot.on_message(filters.command("help"))
async def help_command(client, message):
    try:
        await message.reply_text("ℹ️ Available Commands:\n/start - Start the bot\n/help - Show this help message")
        logger.info(f"✅ Sent help message to {message.from_user.id}")

    except Exception as e:
        logger.error(f"❌ Error in /help command: {e}", exc_info=True)
        await message.reply_text("⚠️ An error occurred! Check logs for details.")

# ✅ Function to log new users in MongoDB
def log_new_user(user_id, username):
    try:
        store_new_user(user_id, username)
        logger.info(f"✅ New user added: {user_id} ({username})")
    except Exception as e:
        logger.error(f"❌ Failed to log user {user_id}: {e}", exc_info=True)

# ✅ Bot main function
async def main():
    try:
        logger.info("🚀 Bot is starting...")
        await bot.start()
        logger.info("✅ Bot started successfully!")

        # ✅ Start the fake web server (for Koyeb health check)
        await server.start_server()

        # ✅ Keep the bot running
        await asyncio.Event().wait()

    except Exception as e:
        logger.critical(f"❌ Bot crashed: {e}", exc_info=True)

# ✅ Run the bot using asyncio.run
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.critical(f"❌ Main execution failed: {e}", exc_info=True)
