from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Ichimliklar_uchuneng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Cola")
        ],
        [
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="tea"),
            KeyboardButton(text="Cofe")

        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)