import telebot
import time
import os

# Configuración segura
TOKEN = '8607330231:AAFcQFP1qB0ItflRC2vevWJYuEH-Q0oBwiw'
MI_ID = 6523912194
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: m.chat.id == MI_ID)
def respuesta(m):
    texto = m.text.lower()
    if 'estado' in texto:
        bot.reply_to(m, "🦾 ARES: Operativo en la Nube 24/7.")
    else:
        bot.reply_to(m, "🦾 ARES: Recibido y procesado.")

# Bucle infinito con auto-reinicio
while True:
    try:
        print(">>> ARES VIGILANDO EN LA NUBE...")
        bot.infinity_polling(timeout=20, long_polling_timeout=10)
    except Exception as e:
        print(f"Error: {e}. Reiniciando en 5s...")
        time.sleep(5)
      
