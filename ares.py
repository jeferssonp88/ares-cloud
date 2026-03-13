import telebot

TOKEN = '8607330231:AAFcQFP1qB0ItflRC2vevWJYuEH-Q0oBwiw'
MI_ID = 6523912194
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: m.chat.id == MI_ID)
def respuesta(m):
    bot.reply_to(m, "🦾 ARES: Te escucho fuerte y claro, jefe. Operativo en la nube.")

print(">>> ARES ESTA VIVO Y TE RECONOCE")
bot.infinity_polling()
