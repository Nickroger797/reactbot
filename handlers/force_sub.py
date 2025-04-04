
async def force_sub_handler(client, message):
    user_id = message.from_user.id
    if message.text.startswith("/start"):
        # Check if user has joined the force subscription channel
        member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        if member.status != "member":
            await message.reply("Please join the mandatory channel to use the bot.")
        else:
            await message.reply("Welcome to the bot!")
