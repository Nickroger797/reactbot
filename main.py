from pyrogram import Client
import logging
import os
from aiohttp import web
from handlers import start, reaction_game, ai_reactions, connect, force_sub
from config import BOT_TOKEN, LOG_CHANNEL, FORCE_SUB_CHANNEL, PORT

# Pyrogram Client
bot = Client("reaction_bot", bot_token=BOT_TOKEN)

# Fake Web Server for Koyeb
async def ping(request):
    return web.Response(text="Bot is running!")

async def start_fake_server():
    app = web.Application()
    app.router.add_get("/", ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

# Log new user to MongoDB
def log_new_user(user_id, username):
    # Function to log user data in MongoDB
    store_new_user(user_id, username)

# Bot Main Function
async def main():
    logging.info("Bot is starting...")
    await bot.start()
    await start_fake_server()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
