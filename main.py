#импортируем библиотеку
import telebot

# создаем переменную + пишем полученный токен
bot = telebot.TeleBot = ('')

#реакция на команду /start
@bot.message_handler(commands=['start'])

#принимаем параметр message от пользователя
def start_message(message):
    #Отправка ответа от бота
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
