import telebot
from telebot import types

API_TOKEN = 'PASTE_YOUR_BOT_TOKEN_HERE'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Купить Stars")
    btn2 = types.KeyboardButton("Поддержка")
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id,
        "Привет! Я бот для покупки Telegram Stars.\nВыберите опцию:",
        reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Купить Stars")
def ask_amount(message):
    bot.send_message(message.chat.id, "Сколько Stars вы хотите купить?")

@bot.message_handler(func=lambda m: m.text.isdigit())
def calculate_price(message):
    stars = int(message.text)
    price = round(stars * 0.012, 2)
    bot.send_message(message.chat.id,
        f"{stars} Stars стоят примерно {price} TON.\n"
        f"Оплатите на TON-кошелёк:\n`EQDxxxx...`\n"
        "После оплаты напишите: @yourusername")

@bot.message_handler(func=lambda m: m.text == "Поддержка")
def support(message):
    bot.send_message(message.chat.id, "Поддержка: @yourusername")

print("Бот запущен.")
bot.polling()