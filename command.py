from pyrogram import filters, handlers
from handlers.start import handle_start
from handlers.reaction_game import reaction_game_handler
from handlers.ai_reactions import ai_reaction_handler
from handlers.connect import connect_handler

def register_handlers(bot):
    # /start command (Force Sub check + Welcome + DB)
    bot.add_handler(handlers.MessageHandler(handle_start, filters.command("start")))

    # /reaction command
    bot.add_handler(handlers.MessageHandler(reaction_game_handler, filters.command("reaction")))

    # /ai_reaction command
    bot.add_handler(handlers.MessageHandler(ai_reaction_handler, filters.command("ai_reaction")))

    # /connect command
    bot.add_handler(handlers.MessageHandler(connect_handler, filters.command("connect")))
