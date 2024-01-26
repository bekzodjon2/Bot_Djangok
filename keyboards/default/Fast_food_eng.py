from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Fastfood_uchuneng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hotdog"),
            KeyboardButton(text="Gamburger")
        ],
        [
            KeyboardButton(text="Lavash"),
            KeyboardButton(text="Chizburger"),
            KeyboardButton(text="Pizza")

        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)