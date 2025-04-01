from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB_CHANNEL

app = Client("reaction_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def is_user_subscribed(client, user_id):
    try:
        member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        if member.status in ["member", "administrator", "creator"]:
            return True
        return False
    except UserNotParticipant:
        return False
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    
    # Check if user is subscribed to the force sub channel
    if not await is_user_subscribed(client, user_id):
        join_button = f"https://t.me/{FORCE_SUB_CHANNEL}"
        await message.reply_text(
            f"⚠️ **Force Subscription Required** ⚠️\n\n"
            f"आपको मेरे बॉट का उपयोग करने से पहले [इस चैनल]({join_button}) को जॉइन करना होगा।\n"
            "जॉइन करने के बाद, /start को फिर से दबाएं।",
            disable_web_page_preview=True
        )
        return
    
    # Define Start Menu Buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📖 Help", callback_data="help")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("➕ Add Me To Your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("🔗 Join My Telegram Group", url=OWNER_GROUP_LINK)]
    ])
    
    # Send Start Message
    await message.reply_text(
        "✅ **Welcome to Reaction Bot!**\nअब आप इस बॉट का उपयोग कर सकते हैं।\nनीचे दिए गए बटन से ऑप्शन चुनें।",
        reply_markup=keyboard
    )

@app.on_callback_query()
async def callback_handler(client, query):
    if query.data == "help":
        await query.message.edit_text(
            "📖 **Help Menu**\n\n"
            "बॉट के सभी कमांड्स और उनके उपयोग को देखने के लिए नीचे दिए गए बटन को दबाएं।",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="start")]
            ])
        )
    
    elif query.data == "about":
        await query.message.edit_text(
            "ℹ️ **About This Bot**\n\n"
            "यह एक Reaction Telegram Bot है जो मैसेजेस पर ऑटोमैटिक रिएक्शन देता है।",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="start")]
            ])
        )

    elif query.data == "start":
        # Re-send the start message with buttons
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📖 Help", callback_data="help")],
            [InlineKeyboardButton("ℹ️ About", callback_data="about")],
            [InlineKeyboardButton("➕ Add Me To Your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton("🔗 Join My Telegram Group", url=OWNER_GROUP_LINK)]
        ])
        await query.message.edit_text(
            "✅ **Welcome to Reaction Bot!**\nअब आप इस बॉट का उपयोग कर सकते हैं।\nनीचे दिए गए बटन से ऑप्शन चुनें।",
            reply_markup=keyboard
        )

if __name__ == "__main__":
    app.run()
