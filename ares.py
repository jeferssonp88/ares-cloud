import telebot
TOKEN = '8607330231:AAFcQFP1qB0ItflRC2vevWJYuEH-Q0oBwiw'
MI_ID = 5668634058
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(func=lambda m: m.chat.id == MI_ID)
def respuesta(m):
    bot.reply_to(m, "🦾 ARES: Conexión total desde la nube, jefe.")
print(">>> ARES ACTIVO")
bot.infinity_polling()
