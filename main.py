import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from txt import txtHi

TOKEN = '6255702149:AAGYcZtZxBx3VSJps6h2ynH0q2Rx0zpkFQM'

bot = AsyncTeleBot(TOKEN)


@bot.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('список команд')
    item2 = types.KeyboardButton('Заметки')
    item3 = types.KeyboardButton('Мои заметки')
    item0 = types.KeyboardButton('Пошел на хуй, не придумал')
    markup.add(item1, item2, item3, item0)

    await bot.reply_to(message, 'Пpивет, {0.first_name}, я бот без имени, Так как у того кто меня придумал нет фантазии..\n...зато блять есть эвтаназия, с явным ожиданием катарсиса'.format(message.from_user),  reply_markup=markup)

@bot.message_handler(content_types=['text'])
async def hutinpuylo(message):
     if message.text == 'Пошел на хуй, не придумал':
        await bot.send_message(message.chat.id, 'Простите, господин, это рофл? Просто если это не рофл, то я твоего деда нахуй нахуй садил')

import asyncio
asyncio.run(bot.polling())

