from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Спросить ИИ", callback_data="generate_text"),
    InlineKeyboardButton(text="Узнать Расписание", callback_data="generate_rasp")],
    [InlineKeyboardButton(text="Краткое содержание", callback_data="generate_recenz"),
    InlineKeyboardButton(text="Краткая информация по предмету", callback_data="generate_shpora")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])