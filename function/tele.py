import os
import telebot
from api import get_response

API_KEY = '5176546940:AAGv5n9ujFCE41AiHhuQ4cWHbEHB2x3S4H0'
chat_id = -493944553

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def greet_message(message):
    bot.reply_to(message, "Chào mừng bạn đến với MaiBot")

@bot.message_handler(commands=['Greet'])
def greet_message(message):
    bot.reply_to(message, "Xin chào!")

@bot.message_handler(func=lambda msg: True)
def chat_gpt(message):
    bot.reply_to(message, str(get_response(message.text)))

bot.infinity_polling()

# if __name__ == '__main__':
    # logfile = open(file_path,"r")
    # loglines = follow(logfile)
    # for line in loglines:
        # print(line)
        # print(type(line))
        # bot.send_message(chat_id, "New log: {log}".format(log=line))