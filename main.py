from telegram.ext import Updater, CommandHandler

TOKEN = '7106945455:AAE-N1dVLp4uVomwuNOaksEMotD1vvHuM9U'

tasks = {

}

def start(update, context):
    user_id = update.message.from_user.id
    if user_id not in tasks:
        tasks[user_id] = []
    message = ('Хуш омадед! Барои илова кардани вазифаҳо! \n\n'
               'Истифода баред /add <номи вазифа> барои илова кардани вазифаҳо.\n')
    update.message.reply_text(message)

def add(update, context):
    user_id = update.message.from_user.id
    task_name = ' '.join(context.args)
    if task_name:
        if user_id not in tasks:
            tasks[user_id] = []
        tasks[user_id].append(task_name)
        update.message.reply_text(f"Вазифа илова карда шуд: {task_name}")
        list(update, context)
    else:
        update.message.reply_text("Лутфан номи вазифаро пешниҳод кунед. Истифода: /add <номи вазифа>")
    
def list(update, context):
    user_id = update.message.from_user.id
    if user_id in tasks and tasks[user_id]:
        task_list = '\n'.join(f"{i+1}. {task}" for i, task in enumerate(tasks[user_id]))
        update.message.reply_text(f"Вазифаҳои шумо:\n{task_list}")
    else:
        update.message.reply_text("Вазифаҳо нест.")
def delete(update, context):
    user_id = update.message.from_user.id
    try:
        task_number = int(context.args[0]) - 1  # Индекси вазифа
        if 0 <= task_number < len(tasks[user_id]):
            removed_task = tasks[user_id].pop(task_number)  # Нест кардани вазифа
            update.message.reply_text(f"Вазифа хориҷ карда шуд: {removed_task}")
            list(update, context)  # Рӯйхатро пас аз нест кардан намоиш диҳед
        else:
            update.message.reply_text("Индекси номатлуб. Лутфан рақами дурустро пешниҳод кунед.")
    except (IndexError, ValueError):
        update.message.reply_text("Лутфан рақами дурусти вазифаро пешниҳод кунед. Истифода: /delete <рақами вазифа>")

def edit(update, context):
    user_id = update.message.from_user.id
    try:
        task_number = int(context.args[0]) - 1  # Индекси вазифа
        new_name = ' '.join(context.args[1:])
        if 0 <= task_number < len(tasks[user_id]) and new_name:
            old_task = tasks[user_id][task_number]
            tasks[user_id][task_number] = new_name
            update.message.reply_text(f"Вазифа аз навсозӣ карда шуд: {old_task} ба {new_name}")
            list(update, context)  # Рӯйхатро пас аз нест кардан намоиш диҳед
        else:
            update.message.reply_text("Рақами вазифа нодуруст ё номи нав мавҷуд нест.")
    except (IndexError, ValueError):
        update.message.reply_text("Истифода: /edit <рақами вазифа> <номи вазифа>")

def help(update, context):
    update.message.reply_text(
        "/start - Номнавис шавед ё бо бот муомила карданро оғоз кунед\n"
        "/add <номи вазифа> - Вазифаи нав илова кунед\n"
        "/list - Рӯйхати вазифаҳо\n"
        "/delete <рақами вазифа> - Вазифаро аз рӯи рақам нест кунед\n"
        "/edit <рақами вазифа> <номи нав> - Вазифаро аз рӯи рақам таҳрир кунед\n"
        "/help - Маълумот оиди барнома, ёрӣ"
        )

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('add', add))
    dispatcher.add_handler(CommandHandler('list', list))
    dispatcher.add_handler(CommandHandler('delete', delete))
    dispatcher.add_handler(CommandHandler('edit', edit))
    dispatcher.add_handler(CommandHandler('help', help))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()