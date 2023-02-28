import telebot
from telebot import types

TOKEN = '6255702149:AAGYcZtZxBx3VSJps6h2ynH0q2Rx0zpkFQM'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('список команд')
    item2 = types.KeyboardButton('Заметки')
    item3 = types.KeyboardButton('Мои заметки')
    item0 = types.KeyboardButton('Пошел на хуй, не придумал')
    markup.add(item1, item2, item3, item0)

    bot.reply_to(message, 'Пpивет, {0.first_name}!'.format(message.from_user),  reply_markup=markup)

@bot.message_handler(content_types=['text'])
def hutinpuylo(message):
    if message.text == 'Пошел на хуй, не придумал':
        bot.send_message(message.chat.id, 'Простите, господин, это рофл? Просто если это не рофл, то я твоего деда нахуй нахуй садил')


bot.polling(none_stop = True)
