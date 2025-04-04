from messages import start_message

async def start_handler(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    # Store user data
    store_new_user(user_id, username)
    await message.reply(start_message)
