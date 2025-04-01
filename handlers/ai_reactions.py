from pyrogram import Client
from reactions import ai_reaction

@Client.on_message()
async def ai_reaction_handler(client, message):
    if message.text.startswith("/ai_reaction"):
        reaction = ai_reaction(message.text)
        await message.reply(f"AI Reaction: {reaction}")
