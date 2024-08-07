from telegram.ext import Updater, CommandHandler

TOKEN = '7249517311:AAFKEqGOkugTiEmeXQ6Q3LrC1ValfilLgv8'

def start(update, context):
    message = ('Telegram бота для управления задача! \n\n'
               '/add - Отправить вам мой контакты.\n'
               '/talk - Суҳбат дар Whatsapp')
    update.message.reply_text(message)

def add(update, context):
    message = '+992 988851282 \n +992 100300658'
    update.message.reply_text(message)

def talk(update, context):
    message = 'Ман ҳоло ҷавоб дода наметавонам. :joy:'
    update.message.reply_text(message)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('add', add))
    dispatcher.add_handler(CommandHandler('talk', talk))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()