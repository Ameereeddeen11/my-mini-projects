from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import datetime
import json
file_path1 = open('C:/Users/Amir/Desktop/Python/bot/uzimiz.json', 'r')
token = json.load(file_path1)
file_path2 = open('C:/Users/Amir/Desktop/Python/bot/birthdays.json', 'r')
#birthday = json.load(file_path2)['tugilgan kun']
date = datetime.date.today()
birthday2 = json.load(file_path2)

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

    elif "amir tugilgan kuni qachon?" in processed:
        return birthday2["Amir"]

    elif "oyimni tugilgan kuni qachon?" in processed:
        return birthday2["Oyim"]

    elif "dadami tugilgan kuni qachon?" in processed:
        return birthday2["Dadam"]

    elif "kimni tugilgan kuni bugun?" in processed:
        closest_diff = datetime.timedelta(days=365)
        closest_person = None
        closest_date = None
        for name, data in birthday2["tugilgan kun"].items():
            birthday_date = datetime.datetime.strptime(data, "%m-%d").date()

            diff = abs(birthday_date - date)
            if 0 <= diff.days < closest_diff.days:
                closest_diff = diff
                closest_date = data
                closest_person = name

        if birthday2 == date:
            return "Bugun ", name, "tugilgan kuni bor"
        else:
            return "Bugun", date.strftime("%m-%d"), "Hech kimni tugilgan kuni yoq. Lekin ", closest_date, " kuna ", closest_person
    else:
        return "I don't know"

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User ({update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if token["BOT_USERNAME"] in text:
            new_text: str = text.replace((token["@BOT_USERNAME"], '')).strip()
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