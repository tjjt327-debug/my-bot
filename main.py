import telebot

TOKEN = "6095098175:AAEpdMXWPON431R00vgDFhUooBfp5DV9qsA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "البوت يعمل يا مهندس علي!")

print("جاري تشغيل البوت...")
bot.polling()
