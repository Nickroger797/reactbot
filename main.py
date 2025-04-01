import logging
import asyncio
import pytz
from datetime import datetime
from pyrogram import Client
from aiohttp import web
from handlers import start, reaction_game, ai_reactions, connect, force_sub
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, PORT, API_ID, API_HASH

# Pyrogram Client with API_ID and API_HASH
bot = Client("reaction_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Fake Web Server for Koyeb (Optional for health check)
async def ping(request):
    # Get the current UTC time and send in the response
    utc_now = datetime.now(pytz.utc)
    return web.Response(text=f"Bot is running! Current UTC Time: {utc_now}")

async def start_fake_server():
    app = web.Application()
    app.router.add_get("/", ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

# Function to check time sync
def check_time_sync():
    # Get the server time (in UTC)
    utc_now = datetime.now(pytz.utc)
    logging.info(f"Current UTC Time: {utc_now}")

# Bot Main Function
async def main():
    logging.info("Bot is starting...")

    # Check server time synchronization
    check_time_sync()

    await bot.start()
    await start_fake_server()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
