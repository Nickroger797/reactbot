from pyrogram import filters
from pyrogram.types import Message
from config import FORCE_SUB_CHANNEL
from pyrogram.errors import UserNotParticipant
from message import WELCOME_MESSAGE  # 👈 यहाँ import किया

async def force_sub_handler(client, message: Message):
    user_id = message.from_user.id
    try:
        # Check if user is a member
        member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            await message.reply(f"Please join the mandatory channel to use the bot:\nhttps://t.me/{FORCE_SUB_CHANNEL}")
            return
    except UserNotParticipant:
        await message.reply(f"Please join the mandatory channel to use the bot:\nhttps://t.me/{FORCE_SUB_CHANNEL}")
        return

    # If user is a member, send welcome message from message.py
    await message.reply(start_message)
