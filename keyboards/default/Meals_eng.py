from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
taomlar_uchuneng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Soup"),
            KeyboardButton(text="Pilaf")
        ],
        [
         KeyboardButton(text="Chicken"),
         KeyboardButton(text="Sandwiches")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)