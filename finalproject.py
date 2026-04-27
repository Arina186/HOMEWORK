import telebot
from telebot import types
import database
import os
from dotenv import load_dotenv
import random

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

BUTTON_ITEM = "➕ Добавить вещь"
BUTTON_WARDROBE = "👗 Мой гардероб"
BUTTON_EXPENSES = "📊 Траты за месяц"
BUTTON_OUTFIT = "🎲 Составить образ на сегодня"
BUTTON_STATISTICS = "📈 Аналитика вашего гардероба"

bot = telebot.TeleBot(TOKEN)


def create_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True)
    button_item = telebot.types.KeyboardButton(BUTTON_ITEM)
    button_wardrobe = telebot.types.KeyboardButton(BUTTON_WARDROBE)
    button_expenses = telebot.types.KeyboardButton(BUTTON_EXPENSES)
    button_out = telebot.types.KeyboardButton(BUTTON_OUTFIT)
    button_statistics = telebot.types.KeyboardButton(BUTTON_STATISTICS)
    keyboard.add(button_item, button_wardrobe, button_expenses, button_out, button_statistics)

    return keyboard


@bot.message_handler(commands=['start'])
def start(message):
    # Подключаемся к базе и регистрируем пользователя
    with database.connect_db() as conn:
        database.register_user(conn, message.from_user.id, message.from_user.username)

    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! Я помогу тебе следить за гардеробом.",
        reply_markup=create_menu()
    )


@bot.message_handler(func=lambda message: message.text == BUTTON_EXPENSES)
def show_spending(message):
    with database.connect_db() as conn:
        spent = database.get_monthly_spending(conn, message.from_user.id)
    bot.send_message(message.chat.id, f"В этом месяце ты потратил(а): {spent} BYN")


@bot.message_handler(func=lambda message: message.text == BUTTON_ITEM)
def choose_category(message):
    with database.connect_db() as conn:
        categories = database.get_categories(conn)

    markup = types.InlineKeyboardMarkup()
    for cat_id, cat_name in categories:
        # в callback_data передается ID категории
        markup.add(types.InlineKeyboardButton(cat_name, callback_data=f"add_cat_{cat_id}"))

    bot.send_message(message.chat.id, "Выбери категорию:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('add_cat_'))
def get_category_callback(call):
    # ID категории из callback_data
    category_id = int(call.data.split('_')[2])

    msg = bot.send_message(call.message.chat.id, "Введите бренд (или напишите 'Нет'):")
    # следующий шаг, передаем ID категории дальше
    bot.register_next_step_handler(msg, process_brand_step, category_id)


def process_brand_step(message, category_id):
    brand = message.text
    msg = bot.send_message(message.chat.id, "Введите стоимость вещи (число):")
    bot.register_next_step_handler(msg, process_price_step, category_id, brand)


def process_price_step(message, category_id, brand):
    try:
        price = float(message.text)
        msg = bot.send_message(message.chat.id, "Отправьте фото вещи:")
        bot.register_next_step_handler(msg, process_photo_step, category_id, brand, price)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Пожалуйста, введите цену цифрами (например, 120.50):")
        bot.register_next_step_handler(msg, process_price_step, category_id, brand)


def process_photo_step(message, category_id, brand, price):
    if message.content_type == 'photo':
        # берем ID самого крупного фото
        photo_id = message.photo[-1].file_id

        with database.connect_db() as conn:
            database.add_item(conn, message.from_user.id, category_id, brand, price, photo_id)

        bot.send_message(message.chat.id, "✅ Вещь успешно сохранена!", reply_markup=create_menu())
    else:
        msg = bot.send_message(message.chat.id, "Нужно отправить именно фото. Попробуйте еще раз:")
        bot.register_next_step_handler(msg, process_photo_step, category_id, brand, price)


@bot.message_handler(func=lambda message: message.text == BUTTON_WARDROBE)
def show_wardrobe(message):
    with database.connect_db() as conn:
        items = database.get_wardrobe(conn, message.from_user.id)

    if not items:
        bot.send_message(message.chat.id, "Твой гардероб пока пуст. Добавь что-нибудь!")
        return

    bot.send_message(message.chat.id, "👗 Твои вещи:")

    for item_id, brand, price, category_name, purchase_date, photo_id, usage_count in items:
        cpw = round(price / usage_count, 2) if usage_count > 0 else price
        caption = (
            f"🏷 **Бренд:** {brand}\n"
            f"📂 **Категория:** {category_name}\n"
            f"💰 **Цена:** {price} BYN\n"
            f"🔄 **Ты надел эту вещь:** {usage_count} раз\n"
            f"📉 **Цена за одну носку:** {cpw} BYN\n"
            f"📅 **Дата покупки:** {purchase_date.strftime('%d.%m.%Y')}"
        )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✅ Надеть сегодня", callback_data=f"wear_{item_id}"))
        markup.add(types.InlineKeyboardButton("🗑 Удалить", callback_data=f"delete_{item_id}"))

        if photo_id:
            bot.send_photo(message.chat.id, photo_id, caption=caption, reply_markup=markup, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, caption, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data.startswith('delete_'))
def handle_delete_item(call):
    item_id = int(call.data.split('_')[1])

    with database.connect_db() as conn:
        # функция удаления из database.py
        database.delete_user_item(conn, call.from_user.id, item_id)

    bot.answer_callback_query(call.id, "Вещь удалена из гардероба")
    bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith('wear_'))
def handle_wear_item(call):
    item_id = int(call.data.split('_')[1])

    with database.connect_db() as conn:
        database.add_usage(conn, item_id)

    bot.answer_callback_query(call.id, "Отлично! Счетчик обновлен.")

    # обновляем цену за одну носку
    bot.edit_message_caption(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        caption=call.message.caption + "\n\n🔄 Обновлено: +1 носка",
        reply_markup=None  # Убираем кнопку после нажатия
    )


@bot.message_handler(func=lambda message: message.text == BUTTON_OUTFIT)
def make_outfit(message):
    with database.connect_db() as conn:
        is_dress_look = random.choice([True, False])

        media = []
        description = "✨ Твой образ на сегодня:\n"
        if is_dress_look:
            dress = database.get_random_item_from_category(conn, message.from_user.id, ['Платья'])
            if dress:
                media.append(telebot.types.InputMediaPhoto(dress[1]))  # photo_id
                description += f"👗 Платье: {dress[0]}\n"
            else:
                is_dress_look = False  # Если платьев нет, откатываемся к комплекту
        if not is_dress_look:
            # сначала выбираем верх лука
            top = database.get_random_item_from_category(conn, message.from_user.id, ["Футболки/Рубашки/Блузки",
                                                                                      "Жакеты и пиджаки",
                                                                                      "Джемперы/Свитеры"])
            bottom = database.get_random_item_from_category(conn, message.from_user.id,
                                                            ["Брюки/Джинсы", "Шорты", "Леггинсы", "Юбки"])
            if top and bottom:
                media.append(telebot.types.InputMediaPhoto(top[1]))
                media.append(telebot.types.InputMediaPhoto(bottom[1]))
                description += f"👕 Верх: {top[0]}\n👖 Низ: {bottom[0]}\n"
            else:
                bot.send_message(message.chat.id, "Добавь больше вещей, чтобы я мог составить образ!")
                return

        outwear = database.get_random_item_from_category(conn, message.from_user.id, ["Верхняя одежда"])
        shoes = database.get_random_item_from_category(conn, message.from_user.id, ["Обувь"])
        accessory = database.get_random_item_from_category(conn, message.from_user.id, ["Аксессуары"])

        if outwear:
            media.append(telebot.types.InputMediaPhoto(outwear[1]))
            description += f"🧥 Сверху: {outwear[0]}\n"
        if shoes:
            media.append(telebot.types.InputMediaPhoto(shoes[1]))
            description += f"👟 Обувь: {shoes[0]}\n"
        if accessory:
            media.append(telebot.types.InputMediaPhoto(accessory[1]))
            description += f"👜 Аксессуар: {accessory[0]}\n"

        media[0].caption = description
        bot.send_media_group(message.chat.id, media)


@bot.message_handler(func=lambda message: message.text == BUTTON_STATISTICS)
def show_full_stats(message):
    with database.connect_db() as conn:
        stats = database.get_wardrobe_stats(conn, message.from_user.id)
        #  траты за месяц
        monthly = database.get_monthly_spending(conn, message.from_user.id)

    if not stats:
        bot.send_message(message.chat.id, "📊 У тебя пока нет вещей для анализа. Добавь что-нибудь!")
        return

    text = (
        f"📊 **Аналитика твоего гардероба**\n\n"
        f"👗 Всего вещей: {stats['total_count']} шт.\n"
        f"💰 Общая стоимость: {stats['total_sum']} BYN\n"
        f"💵 Средняя цена вещи: {stats['avg_price']} BYN\n"
        f"🔝 Самая дорогая: {stats['max_price']} BYN\n"
        f"📉 Самая бюджетная: {stats['min_price']} BYN\n\n"
        f"📅 Траты за последние 30 дней: {monthly} BYN"
    )

    bot.send_message(message.chat.id, text, parse_mode="Markdown")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
