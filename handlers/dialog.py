from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
from utils.fill_template import fill_template
from utils.generate_pdf import convert_to_pdf
import datetime
import uuid
import os

DATE, SENDER, RECEIVER, ITEMS = range(4)
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Введіть дату (наприклад, 06.07.2025):")
    return DATE

async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data['date'] = update.message.text
    await update.message.reply_text("Введіть наименування грузоотправителя:")
    return SENDER

async def get_sender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data['sender'] = update.message.text
    await update.message.reply_text("Введіть наименування грузополучателя:")
    return RECEIVER

async def get_receiver(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data['receiver'] = update.message.text
    await update.message.reply_text("Введіть список товарів (в форматі: наименування - кількість - маса):")
    return ITEMS

async def get_items(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data['items'] = update.message.text
    docx_path = fill_template(user_data)
    # pdf_path = convert_to_pdf(docx_path)
    # await update.message.reply_document(document=open(pdf_path, 'rb'))
    await update.message.reply_document(document=open(docx_path, 'rb'))
    await update.message.reply_text("Документ сформовано.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Операція скасована.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Тест")

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    test_data = {
        'date': datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        'sender': str(uuid.uuid4()),
        'receiver': str(uuid.uuid4()),
        'items': str(uuid.uuid4())
    }
    docx_path = fill_template(test_data)
    pdf_path = convert_to_pdf(docx_path)
    print("test_command pdf_path:", pdf_path)

    # await update.message.reply_document(document=open(pdf_path, 'rb'))
    await update.message.reply_document(document=open(docx_path, 'rb'))
    await update.message.reply_text("Тестова ТТН сгенерована.")
    return ConversationHandler.END
    
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),CommandHandler('test', test_command),],
    states={
        DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_date)],
        SENDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_sender)],
        RECEIVER: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_receiver)],
        ITEMS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_items)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)