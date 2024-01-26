from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Ichimliklar_uchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Cola")
        ],
        [
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="Choy"),
            KeyboardButton(text="Cofe")

        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)