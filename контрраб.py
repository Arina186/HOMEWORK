#task 2
import os
from dotenv import load_dotenv
import telebot
import json
from random import choice
from text_to_speech import text_to_speech, speech_to_text

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

BUTTON_VERBS = "New words"
BUTTON_IDIOMS = "New idioms"

bot = telebot.TeleBot(TOKEN)

def create_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True)
    button_verbs = telebot.types.KeyboardButton(BUTTON_VERBS)
    button_idioms = telebot.types.KeyboardButton(BUTTON_IDIOMS)
    keyboard.add(button_verbs, button_idioms)

    return keyboard

def get_quiz_by_level(level):
    try:
        with open('questions.json', 'r', encoding='utf-8') as f:
            all_questions = json.load(f)
        if isinstance(level, list):
            filtered = [q for q in all_questions if q.get('level') in level]
        else:
            filtered = [q for q in all_questions if q.get('level') == level]
        if filtered:
            return choice(filtered)
        return None
    except Exception as e:
        print(f"Ошибка загрузки JSON: {e}")
        return None


def send_quiz_poll(chat_id, item):
    bot.send_poll(
        chat_id=chat_id,
        question=f"[{item['level']}] {item['question']}",
        options=item['options'],
        type='quiz',
        correct_option_id=item['correct_id'],
        is_anonymous=False
    )


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
    "Привет, я бот, который поможет улучшить тебе английский язык! \n Мои команды:\n "
        "/start - запуск бота\n"
        "/help - справка\n"
        "/quizeasy - тест для уровня A1\n"
        "/quizmedium - тест для уровня B1,B2\n"
        "/quizhard - тест для уровня C1\n"
        "/pronunciation - отправь мне текст, чтобы узнать правильное произношение!\n",
        reply_markup = create_menu()
                        )



@bot.message_handler(commands=['quizeasy'])
def easy_quiz(message):
    item = get_quiz_by_level("A1")
    if item:
        send_quiz_poll(message.chat.id, item)

        bot.send_message(
            message.chat.id,
            "Удачи в тесте! Выбери вариант ответа выше 👆",
            reply_markup=create_menu()
        )
    else:
        bot.reply_to(message, "Вопросы уровня A1 не найдены")


@bot.message_handler(commands=['quizmedium'])
def medium_quiz(message):
    item = get_quiz_by_level(["B1", "B2"])
    if item:
        send_quiz_poll(message.chat.id, item)

        bot.send_message(
            message.chat.id,
            "Удачи в тесте! Выбери вариант ответа выше 👆",
            reply_markup=create_menu()
        )
    else:
        bot.reply_to(message, "Вопросы уровня B2 не найдены")

@bot.message_handler(commands=['quizhard'])
def hard_quiz(message):
    item = get_quiz_by_level("C1")
    if item:
        send_quiz_poll(message.chat.id, item)

        bot.send_message(
            message.chat.id,
            "Удачи в тесте! Выбери вариант ответа выше 👆",
            reply_markup=create_menu()
        )
    else:
        bot.reply_to(message, "Вопросы уровня C1 не найдены")


@bot.message_handler(func=lambda message: message.text == BUTTON_VERBS)
def handle_button_words(message):
    verbs = [
        "To refute - [rɪˈfjuːt] - Опровергать",
        "To pluck - [plʌk] - Вырывать",
        "To mold - [məʊld] - Лепить",
        "To supersede - [ˌsjuːpəˈsiːd] - Вытеснять",
        "To reminisce - [ˌrɛmɪˈnɪs] - Вспоминать",
        "To venerate - [ˈvɛnəreɪt] - Почитать",
        "To overlook - [ˌəʊvəˈlʊk] - Упускать из виду",
        "To redeem - [rɪˈdiːm] - Выкупить",
        "To abjure - [əbˈʤʊə] - Отказаться",
        "To disabuse - [ˌdɪsəˈbjuːz] - Разочаровать, расстроить",
        "To dismantle - [dɪsˈmæntl] - Демонтировать, разобрать",
        "To exhilarate - [ɪgˈzɪləreɪt] - Взбодриться",
        "To mitigate - [ˈmɪtɪgeɪt] - Смягчать, сгладить",
        "To indulge - [ɪnˈdʌlʤ] - Побаловать, потакать",
        "To eradicate - [ɪˈrædɪkeɪt] - Искоренить"

    ]

    selected_verb = choice(verbs)
    response = f"**ADVANCED VERB**\n{selected_verb}"
    bot.send_message(
        message.chat.id,
        response,
        parse_mode="Markdown",
        reply_markup=create_menu()
    )


@bot.message_handler(func=lambda message: message.text == BUTTON_IDIOMS)
def handle_button_anecdote(message):
    idioms = [
        "A bundle of nerves  —  комок нервов, очень нервный человек",
        "Go the extra mile — приложить дополнительные усилия",
        "Play hooky —   прогуливать (школу, занятия, работу)",
        "Keep head above the water —   оставаться на плаву; преодолевать сложности ",
        "Have one’s head in cloud — витать в облаках; быть рассеянным",
        "Full of beans — в приподнятом настроении; оживленный",
        "Fly off the handle — потерять над собой контроль; пойти вразнос",
        "Get peeved  — выйти из себя, впасть в ярость",
        "From the horse's mouth - из первых рук",
        "To break the ice - разрядить обстановку",
        "The icing on the cake - вишенка на торте",
        "To be all ears — весь во внимании",
        "Bad blood  —  взаимная неприязнь; ненависть",
        "Cut from the same cloth — два сапога пара",
        "Live off the grid — жить вдали от суеты, от благ цивилизации"

    ]

    selected_idiom = choice(idioms)
    response = f"**NEW IDIOM**\n{selected_idiom}"
    bot.send_message(
        message.chat.id,
        response,
        parse_mode="Markdown",
        reply_markup=create_menu()
    )



@bot.message_handler(commands=['pronunciation'])
def pronounce(message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        return bot.reply_to(message, "Напиши текст, например: /pronunciation Hello!")

    text_to_say = args[1]
    user_id = message.chat.id

    audio_file = text_to_speech(text_to_say, user_id)
    try:
       with open(audio_file, "rb") as f:
           bot.send_audio(message.chat.id, audio=f, caption="Произношение")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при отправке: {e}")
    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)

@bot.message_handler(content_types=['voice'])
def voice_to_text(message):
    chat_id = message.chat.id
    file = bot.get_file(message.voice.file_id)
    downloaded_bytes = bot.download_file(file.file_path)
    ogg_filename = f"voice_{chat_id}.ogg"
    with open(ogg_filename, "wb") as f:
        f.write(downloaded_bytes)
    text = speech_to_text(ogg_filename)
    bot.send_message(chat_id, text=f"Вы сказали: {text}")

    if os.path.exists(ogg_filename):
        os.remove(ogg_filename)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(
        message.chat.id,
        "Я вас не понял, используйте команды /start или /help"
    )

bot.infinity_polling()