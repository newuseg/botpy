import telebot

Token = "6911484112:AAHd4u5vZ7lvwyayrgCT2F1CBZJmxqBssTg"

bot = telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "Welcome")

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message, """/start -> Greeting
    /help -> will all commands list
    If want to use it as calculator""")

@bot.message_handler()
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "can't be evaluated"
    bot.reply_to(message,msg)

bot.polling()