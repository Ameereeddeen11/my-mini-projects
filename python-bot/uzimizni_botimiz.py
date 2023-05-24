from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import date
import json
file_path1 = open('C:/Users/Amir/Desktop/Python/bot/uzimiz.json', 'r')
token = json.load(file_path1)

#commands
async def start_command (update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! What would you know?")

async def help_command (update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ask me to someones birthday")

async def custom_command (update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! What would you know?")


#responses
def handle_response(text:str):
    processed: str = text.lower()
    if 'hello' in processed:
        return 'hello there! ask me to someones birthday'

    elif "amir" in processed:
        return "03.03.2005"

    else:
        return "I don't know"

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User ({update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if token["BOT_USERNAME"] in text:
            new_text: str = text.replace((token["BOT_USERNAME"], '')).strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('BOT:', response)
    await update.message.reply_text(response)

async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot ...')
    app = Application.builder().token(token["TOKEN"]).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    #polls the bot
    print('Polling...')
    app.run_polling(poll_interval=5)