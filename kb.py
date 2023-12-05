from aiogram.types import InlineKeyboardButton, inline_keyboard_markup, KeyboardButton, reply_keyboard_markup, reply_keyboard_remove
menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    #[InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    #InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
    #InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    #[
    InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = inline_keyboard_markup(inline_keyboard=menu)
exit_kb = reply_keyboard_markup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = inline_keyboard_markup(inline_keyboard=[[KeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
