import telebot
from telebot import types
import sqlite3 #импортировал херь для работы с базой данных

TOKEN = '6255702149:AAGYcZtZxBx3VSJps6h2ynH0q2Rx0zpkFQM'

bot = telebot.TeleBot(TOKEN)

db = sqlite3.connect('Notes.db')# Создал файл где будут хранится данные


db.close()
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #item1 = types.KeyboardButton('Список команд') Не вижу в ней смысла
    item2 = types.KeyboardButton('Добавить заметку')
    item3 = types.KeyboardButton('Мои заметки')
    item0 = types.KeyboardButton('Пошел на хуй, не придумал')
    markup.add(item2, item3, item0)

    bot.reply_to(message, 'Пpивет, {0.first_name}!'.format(message.from_user),  reply_markup=markup)

@bot.message_handler(content_types=['text'])
def hutinpuylo(message):
    if message.text == 'Пошел на хуй, не придумал':
        bot.send_message(message.chat.id, 'Простите, господин, это рофл? Просто если это не рофл, то я твоего деда нахуй нахуй садил')


bot.polling(none_stop = True)
