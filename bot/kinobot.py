import telebot
from telebot import types

from bot.config import TELEGRAM_TOKEN
from bot.utils.keyboard import generate_markup
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from db.Users import User

bot = telebot.TeleBot(TELEGRAM_TOKEN)


def start_bot():
    bot.infinity_polling()
    bot.stop_bot()


commands = {
    "start": ["/start"],
    "kino": ["/kino", "Поехали!"],
    "add_to_favorite": ["/add_to_favorite"],
    "show_favorite": ["/show_favorite"],
    "delete_from_favorite": ["/delete_from_favorite"],
    "info": ["/info"],
}


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    chat_id = message.chat.id

    user = User(user_id, user_name, chat_id)
    markup = None
    if user.is_exist():
        hello_msg = f"✅ Так, вы уже есть в нашей базе, давайте выбирать фильмы, готовы? /kino"

        btn = KeyboardButton('Поехали!')

        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(btn)
    else:
        hello_msg = f"🎬 Кинобот приветствует тебя, {user_name}!\n" \
                    f"🎬 Я буду присылать тебе фильмы,\nа ты выбирай какие из них хотел бы посмотреть!\n" \
                    f"🎬 Чтобы посмотреть все доступные команды напиши /info" \
                    f"\n\n <b>Чтобы начать введите команду /kino </b>"
        user.add()

    bot.send_message(chat_id, hello_msg, parse_mode='HTML', reply_markup=markup)


@bot.message_handler(commands=['kino'])
def kino(message):
    user_id = message['from_user']['id']
    user_name = message['from_user']['username']
    chat_id = message['chat']['id']
    bot.send_message(chat_id, "Кино", parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def text_handler(message):

    # Проверка на совпадение текста и команды
    for key, val in commands.items():
        if message.text in val:
            command = key
            break
    func = f"{command}({message})"
    eval(func)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call)
    print(call.message)
    print(call.data)
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")


@bot.message_handler(commands=['info'])
def start(message):
    chat_id = message.chat.id
    msg = f"Доступные команды:\n ➡️ /kino - показать новые фильмы\n" \
                f" ➡️ /add_to_favorite - добавить фильм в коллекцию\n" \
                f" ➡️ /show_favorite - показать мою коллекцию\n" \
                f" ➡️ /delete_from_favorite - удалить фильм из коллекции\n" \
                f" ➡️ /info - показать доступные команды"
    bot.send_message(chat_id, msg)
