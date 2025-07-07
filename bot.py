from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
from handlers.dialog import conv_handler
import config

if __name__ == '__main__':
    app = ApplicationBuilder().token(config.TOKEN).build()
    app.add_handler(conv_handler)
    app.run_polling()
