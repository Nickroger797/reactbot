from pyrogram import Client

@Client.on_message()
async def connect_handler(client, message):
    if message.text.startswith("/connect"):
        group_id = message.text.split()[1]
        await client.join_chat(group_id)
        await message.reply(f"Bot connected to group {group_id} successfully!")
