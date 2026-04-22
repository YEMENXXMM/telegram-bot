import telebot
import os

# ضع التوكن الخاص بك هنا
API_TOKEN = '8719879208:AAG7vy5_pEUnU9yLThWdicJdAUY0rWaOmT8'
bot = telebot.TeleBot(API_TOKEN)

def telegram_bot(request):
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.get_json(force=True))
        bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً! هذا البوت يعمل على سحابة جوجل للأبد ☁️")
