import asyncio
import logging
from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, MONGO_URI
from pymongo import MongoClient
import db

# ✅ Logging setup
logging.basicConfig(
    level=logging.DEBUG,  
    format="%(asctime)s - [%(levelname)s] - %(message)s",
)
logger = logging.getLogger(__name__)

# ✅ MongoDB Connection
try:
    client = MongoClient(MONGO_URI)
    db = client["reaction_bot"]
    users_col = db["users"]
    logs_col = db["conversion_logs"]
    client.server_info()
    print("\u2705 MongoDB Connected Successfully!")
except Exception as e:
    print("\u274c MongoDB Connection Error:", e)
    exit(1)

# ✅ Check if Variables Exist
if not all([BOT_TOKEN, API_ID, API_HASH, MONGO_URI]):
    logger.critical("❌ BOT_TOKEN, API_ID, API_HASH missing! Check config.py")
    exit(1)

# ✅ Pyrogram Client
bot = Client(
    name="reaction_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ✅ Start Command Handler (With Debugging)
@bot.on_message(filters.command("start"))
async def start(client, message):
    logger.info(f"📩 Received /start from {message.from_user.id}")
    await message.reply_text("👋 Hello! I'm alive and working!")

# ✅ Main function
async def main():
    try:
        logger.info("🚀 Bot is starting...")
        await bot.start()
        me = await bot.get_me()  # Check bot identity
        logger.info(f"✅ Bot started as {me.first_name} (@{me.username})")
        await asyncio.Event().wait()  # Keep bot running
    except Exception as e:
        logger.critical(f"❌ Main execution failed: {e}", exc_info=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.critical(f"❌ Asyncio failed: {e}", exc_info=True)
