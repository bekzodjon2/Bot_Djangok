from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛Taomlar🍛"),
            KeyboardButton(text="🍻Ichimliklar🍻"),
        ],
        [
            KeyboardButton(text="🥞Shirinliklar🥞"),
            KeyboardButton(text="🍔Fastfood🍔"),
            KeyboardButton(text="🍜Arzon taomlar🍜")
        ]
    ],
    resize_keyboard=True
)
