from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛Meals🍛"),
            KeyboardButton(text= "🍻Drinks🍻"),
        ],
        [
            KeyboardButton(text="🥞Sweets🥞"),
            KeyboardButton(text="🍔Fastfood🍔"),
            KeyboardButton(text="🍜Cheap foods🍜")
        ]
    ],
    resize_keyboard=True
)