from pyrogram import Client
from reactions import reaction_game

@Client.on_message()
async def reaction_game_handler(client, message):
    if message.text.startswith("/reaction"):
        reaction = reaction_game()
        await message.reply(f"Your reaction: {reaction}")
