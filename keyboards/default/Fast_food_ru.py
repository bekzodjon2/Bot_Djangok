from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Fastfood_uchunru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Хот дог"),
            KeyboardButton(text="Гамбургер")
        ],
        [
            KeyboardButton(text="Лаваш"),
            KeyboardButton(text="Чизбургер"),
            KeyboardButton(text="Пица")

        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)