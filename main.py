import telebot
import cfg




bot = telebot.TeleBot(cfg.token)


#команды '/start' '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'ИДИ НАХУЙ')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Че тупой шо ль иди нахуй пень ебаный')


# распознования остального как обычный текст
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()