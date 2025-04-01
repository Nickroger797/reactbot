import logging
import asyncio
from pyrogram import Client
from aiohttp import web
from handlers import start, reaction_game, ai_reactions, connect, force_sub
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, PORT, API_ID, API_HASH

# Pyrogram Client with API_ID and API_HASH
bot = Client("reaction_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Fake Web Server for Koyeb (Optional for health check)
async def ping(request):
    return web.Response(text="Bot is running!")

async def start_fake_server():
    app = web.Application()
    app.router.add_get("/", ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

# Bot Main Function
async def main():
    logging.info("Bot is starting...")
    await bot.start()
    await start_fake_server()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
