import telebot

bot = telebot.TeleBot('') # создаем переменную + пишем полученный токен

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start') #Отправка ответа от бота

@bot.message_handler(content_types=['text']) #учим бота отвечать на простые запросы
def send_text(message):
    if message.text == 'Привет':
            bot.send_message(message.chat.id, 'Привет, друг')
    elif message.text == 'Как тебя зовут':
            bot.send_message(message.chat.id, 'Меня зовут Роксанна, я бот')
    elif message.text == 'Пока':
            bot.send_message(message.chat.id, 'До связи')

bot.polling() #Запускает бота, бот проверяет сервер на наличие сообщений
