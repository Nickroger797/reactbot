import asyncio
import logging
import os
from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH

# ✅ Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
)
logger = logging.getLogger(__name__)

# ✅ Pyrogram Client
bot = Client(
    name="reaction_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ✅ Start Command Handler (Simplified)
@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Hello! I'm alive and working!")

# ✅ Main function
async def main():
    logger.info("🚀 Bot is starting...")
    await bot.start()
    logger.info("✅ Bot started successfully!")
    await asyncio.Event().wait()  # Keep bot running

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.critical(f"❌ Main execution failed: {e}", exc_info=True)
