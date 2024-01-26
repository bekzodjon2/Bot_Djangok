from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_uchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛Taomlar🍛"),
            KeyboardButton(text= "🍻Ichimliklar🍻"),
        ],
        [
            KeyboardButton(text="🥞Shirinliklar🥞"),
            KeyboardButton(text="🍔Fast food🍔"),
            KeyboardButton(text="🍜Arzon taomlar🍜")
        ]
    ],
    resize_keyboard=True
)
