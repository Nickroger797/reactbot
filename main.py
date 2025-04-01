from pyrogram import Client
import asyncio
import logging
from handlers import start, reaction_game, ai_reactions, connect, force_sub
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, API_ID, API_HASH

# Pyrogram Client with API_ID and API_HASH
bot = Client("reaction_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Log new user to MongoDB
def log_new_user(user_id, username):
    # Function to log user data in MongoDB
    store_new_user(user_id, username)

# Bot Main Function
async def main():
    logging.info("Bot is starting...")
    await bot.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
