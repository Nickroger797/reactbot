import logging
import threading
from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, MONGO_URI
from db import store_new_user  
import server  # Web server import

# ✅ Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Pyrogram Client
bot = Client("reaction_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ Start Command Handler
@bot.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or "Unknown"
    
    logger.info(f"📩 Received /start from {user_id} (@{username})")
    
    # Save user to database
    try:
        store_new_user(user_id, username)
    except Exception as e:
        logger.error(f"Failed to store user {user_id}: {e}")

    await message.reply_text("👋 Hello! I'm alive and working!")

# ✅ Start fake web server in a separate thread
def start_web_server():
    server.start_server()  # अब यह सही से चलेगा

# ✅ Run the bot
if __name__ == "__main__":
    logger.info("🚀 Bot is starting...")

    # Start the web server in a separate thread
    threading.Thread(target=start_web_server, daemon=True).start()

    # Start the bot
    bot.run()
