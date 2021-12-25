import telebot 
#import os
from glob import glob
from random import choice
from PIL import Image
from telebot import types
bot = telebot.TeleBot('5005174315:AAF7IsBj-kySwgLQYatTpahsoarJf0nw7mc')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Press to die from cringe")
markup.add(item1)


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, "Be prepared", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Press to die from cringe":
        lists = glob('files/*')
        picture = choice(lists)
        img = Image.open(picture)
        bot.send_photo(message.chat.id, img, reply_markup=markup)


bot.polling(none_stop=True, interval=0)

