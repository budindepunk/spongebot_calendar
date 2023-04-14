import os
import telebot
# from get_image import make_image
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('bot_token')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "hello"])
def start_hello(message):
    bot.reply_to(message, "🫡")

@bot.message_handler(commands=["date", "sponge"])
def bot_date(message):
    text = "would you like to know the date?\n yes / no"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode = "Markdown")
    bot.register_next_step_handler(sent_msg, what_do)

formas_de_decir_que_si = ["yes", "si", "sí", "yes!", "si!", "sí!", "¡si!", "¡sí!", "sabelo", "de una", "obvio", "mas bien", "claro", "más bien", "por favor", "you bet", "definitely", "obviously", "naturally", "of course"]
formas_de_decir_que_no = ["no", "No", "no!", "¡no!"]

def what_do(message):
    if message.text.lower() in formas_de_decir_que_si:
        bot.send_message(message.chat.id, "on it")
    elif message.text.lower() in formas_de_decir_que_no:
        bot.send_message(message.chat.id, "ok 😔")
    else: 
        bot.send_message(message.chat.id, "please do not take me beyond my preparation")

@bot.message_handler(func=lambda msg: True)
def other_messages(message):
    bot.reply_to(message, "i do not understand the nuances of human language 🤖😞\ntype /date so i can fulfill my purpose")

bot.infinity_polling()