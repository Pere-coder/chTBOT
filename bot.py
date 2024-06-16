import os
import telebot
from translate import Translator


from dotenv import load_dotenv, dotenv_values

load_dotenv()

BOT_TOKEN=os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

user_language = {}

def get_language(lang, text):
    translator = Translator(from_lang="en", to_lang=lang)
    translation= translator.translate(text)
    return translation


@bot.message_handler(commands=["start","help"])
def lang_handler(message):
    text = ("Hi there, welcome to telegram translate.\n"
            "Just say anything and I'll translate to your preferred language.\n"
            "The format is simple, type language and the short code.\n"
            "Example: /lang fr \n is set to French.\n"
            "Example: /lang en \n is set to English.\n"
            "Here is a list of some country short codes to help you get started:\n"
            "country: French short code: fr\n"
            "country: India short code: in\n"
            "country: English short code: en\n"
            "country: Spanish short code: es\n"
            "country: German short code: de\n"
            "country: Italian short code: it\n"
            "country: Portuguese short code: pt\n"
            "country: Russian short code: ru\n"
            "country: Chinese short code: zh\n"
            "country: Simplified Chinese short code: zh-Hans\n"
            "country: Traditional Chinese short code: zh-Hant\n"
            "country: Japanese short code: ja\n"
            "country: Korean short code: ko\n"
            "country: Arabic short code: ar\n")
    bot.reply_to(message, text)


@bot.message_handler(commands=['lang'])
def set_lang(message):
    try:
        lang_code = message.text.split()[1]
        user_language[message.chat.id] = lang_code
        bot.reply_to(message, f'Language has been set to {lang_code}')
    except IndexError:
        bot.reply_to(message, "Please provide a valid language to translate to")

@bot.message_handler(func=lambda message: True)
def echo_lang(message):
    user_id = message.chat.id
    lang = user_language.get(user_id, "en")
    text = get_language(lang, message.text)
    bot.reply_to(message, text)


bot.infinity_polling()