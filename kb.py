from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

def create_menu():
    menu_buttons = [
        InlineKeyboardButton(text="🗿 Спросить ИИ", callback_data="generate_text"),
        InlineKeyboardButton(text="📆 Узнать расписание", callback_data="generate_rasp"),
        InlineKeyboardButton(text="📋 Краткое содержание лекции", callback_data="generate_recenz"),
        InlineKeyboardButton(text="📝 Краткая информация по предмету", callback_data="generate_shpora"),
        InlineKeyboardButton(text="🔎 Помощь", callback_data="help")
    ]
    return InlineKeyboardMarkup(inline_keyboard=[menu_buttons])

def create_exit_kb():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)

def create_inline_exit_kb():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])


