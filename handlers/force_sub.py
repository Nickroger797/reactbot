from pyrogram import filters
from pyrogram.types import Message
from config import FORCE_SUB_CHANNEL

from pyrogram.errors import UserNotParticipant

async def force_sub_handler(client, message: Message):
    if message.text.startswith("/start"):
        user_id = message.from_user.id
        try:
            member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
            if member.status != "member":
                await message.reply("Please join the mandatory channel to use the bot.")
                return
        except UserNotParticipant:
            await message.reply(f"Please join the mandatory channel to use the bot:\nhttps://t.me/{FORCE_SUB_CHANNEL}")
            return

        await message.reply("Welcome to the bot!")
