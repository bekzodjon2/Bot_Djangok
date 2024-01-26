from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_uchun2eng = ReplyKeyboardMarkup(
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