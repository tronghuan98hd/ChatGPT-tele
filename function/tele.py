import os
import telebot
from api import get_response
import valiable

bot = telebot.TeleBot(valiable.API_KEY)

@bot.message_handler(commands=['start'])
def greet_message(message):
    bot.reply_to(message, "Chào mừng bạn đến với MaiBot")

@bot.message_handler(commands=['Greet'])
def greet_message(message):
    bot.reply_to(message, "Xin chào!")

#add GPT function
@bot.message_handler(func=lambda msg: True)
def chat_gpt(message):
    bot.reply_to(message, str(get_response(message.text)))

bot.infinity_polling()
