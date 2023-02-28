import telebot

TOKEN = '6255702149:AAGYcZtZxBx3VSJps6h2ynH0q2Rx0zpkFQM'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def strat(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('список команд')
    item2 = telebot.types.KeyboardButton('Заметки')
    item3 = telebot.types.KeyboardButton('Мои заметки')
    item0 = telebot.types.KeyboardButton('Пошел на хуй, не придумал')
    markup.add(item1, item2, item3, item0)

    bot.send_message(message.chat.id, 'Пpивет, {0.first_name}!', format(message.from_user), reply_markup=markup)

bot.polling(none_stop = True)

