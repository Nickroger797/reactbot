from pyrogram import filters
from pyrogram.types import Message
from config import FORCE_SUB_CHANNEL
from pyrogram.errors import UserNotParticipant

async def force_sub_handler(client, message: Message):
    user_id = message.from_user.id
    try:
        # Check if user is a member
        member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            await message.reply(f"Please join the mandatory channel to use the bot:\nhttps://t.me/{FORCE_SUB_CHANNEL}")
            return  # 👈 यहाँ return करने से आगे का कोड execute नहीं होगा!
    except UserNotParticipant:
        await message.reply(f"Please join the mandatory channel to use the bot:\nhttps://t.me/{FORCE_SUB_CHANNEL}")
        return  # 👈 यहाँ return करने से आगे का कोड execute नहीं होगा!
    
    # If user is a member, show welcome message
    await message.reply("Welcome to the Reaction Bot! 🤖\nHere are the commands you can use:\n1. /help - Get a list of all commands.\n2. /about - Information about the bot.\n3. /connect - To connect this bot to a group.\n4. /reaction - Use reaction commands.\nEnjoy!")
