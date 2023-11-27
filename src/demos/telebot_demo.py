import telebot
from utils import get_environment_variable

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.talk_status = None


BOT_TOKEN = get_environment_variable("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hi'])
def send_welcome(message: telebot.types.Message):
    """
    Respond to the '/start' and '/hi' commands with a welcome message.

    Args:
        message (telebot.types.Message): The message object representing the user's command.
    """
    welcome_message = "Hola, ¿con quién tengo el gusto de hablar? 😊"
    bot.reply_to(message, welcome_message)
    bot.register_next_step_handler(message, process_name_step)


@bot.message_handler(commands=['end', 'bye'])
def send_goodbye(message: telebot.types.Message):
    """
    Respond to the '/end' and '/bye' commands with a welcome message.

    Args:
        message (telebot.types.Message): The message object representing the user's command.
    """
    goodbye_message = "Chao, espero que la demo haya salido bien. ¡Nos vemos pronto! 😉"
    bot.reply_to(message, goodbye_message)


def process_name_step(message: telebot.types.Message):
    """
    Process the user's name input and set up the next step.

    Args:
        message (Message): The user's message.
    Returns:
        None
    """
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user

        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Muy bien 🥳', 'Regulinchi', 'Mal 🥺')

        reply_message = f"¡Hombre, {name}! ¿Qué tal está yendo la charla?"
        msg = bot.reply_to(message, reply_message, reply_markup=markup)

        bot.register_next_step_handler(msg, process_talk_step)
    except Exception as e:
        bot.reply_to(message, 'Upsi, ha debido de haber algún problema')


def process_talk_step(message: telebot.types.Message):
    """
    Process the user's talk status input and respond accordingly.

    Args:
        message (Message): The user's message.

    Returns:
        None
    """
    try:
        chat_id = message.chat.id
        talk_status = message.text
        user = user_dict.get(chat_id)

        if user:
            if talk_status in ['Regulinchi', 'Mal 🥺']:
                msg = bot.send_message(
                    chat_id, f"Venga {user.name}, seguro que no van tan mal. ¡A por todas! 💪. ¿Quieres que sigamos con la demo?")
            else:
                msg = bot.send_message(
                    chat_id, f"Genial {user.name}, ¡espero que siga así! 🚀. ¿Quieres que sigamos con la demo?")
            bot.register_next_step_handler(msg, process_continue_demo_step)

    except Exception as e:
        bot.reply_to(message, 'Upsi, ha debido de haber algún problema')


def process_continue_demo_step(message: telebot.types.Message):
    """
    Process the user's talk status input and respond accordingly.

    Args:
        message (Message): The user's message.

    Returns:
        None
    """
    try:
        continue_demo = message.text

        if continue_demo == "Sí":
            bot.reply_to(
                message, f"¡Pues vamos allá, envíame distintos tipos de archivos!")
        else:
            bot.reply_to(
                message, f"¿Cómo que no...? No me programaron para eso, envíame distintos tipos de archivos, ¡anda!")
    except Exception as e:
        bot.reply_to(message, 'Upsi, ha debido de haber algún problema')


@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'voice', 'location', 'contact'])
def detects_message_content_type(message):
    """
    Detects imessage_content_type. The content type content_type can be one of the following strings:
    text, audio, document, photo, sticker, video, video_note, voice, location, contact...

    Args:
        message (telebot.types.Message): The message object sent by the user.
    """
    content_type = message.content_type
    bot.reply_to(message, f"Me has enviado un archivo de tipo: {content_type}")


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()
