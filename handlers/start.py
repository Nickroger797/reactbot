from pyrogram import Client
from db import store_new_user  
from messages import log_new_user_message  
from config import LOG_CHANNEL, FORCE_SUB_CHANNEL  
from commands import start_command  # ✅ Command को Import किया

async def is_subscribed(client, user_id):
    """Check if user is subscribed to the Force Sub channel."""
    try:
        chat_member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except:
        return False

async def handle_start(client, message):
    """Start Command Logic"""
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"

    # ✅ Force Sub Check
    if not await is_subscribed(client, user_id):
        return await message.reply("❌ **पहले हमारे चैनल को जॉइन करें!**\n"
                                   f"👉 [Join Now](https://t.me/YourChannel)")

    # ✅ User को Database में Save करो
    store_new_user(user_id, username)

    # ✅ Log Channel में New User Info भेजो
    log_text = log_new_user_message.format(username=username, user_id=user_id)
    await client.send_message(LOG_CHANNEL, log_text)

    # ✅ Start Command Execute करो
    await start_command(client, message)
