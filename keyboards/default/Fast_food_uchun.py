from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Fastfood_uchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hotdog"),
            KeyboardButton(text="Gamburger")
        ],
        [
            KeyboardButton(text="Lavash"),
            KeyboardButton(text="Chizburger"),
            KeyboardButton(text="Pitsa")

        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)