from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Shirinliklar_uchuneng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Candy Room"),
            KeyboardButton(text="Hard candy")
        ],
        [
            KeyboardButton(text="Cotton candy"),
            KeyboardButton(text="Chocolate"),
            KeyboardButton(text="Hallowen Candy")

        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)