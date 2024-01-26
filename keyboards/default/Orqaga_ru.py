from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Orqaga_uchun_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛Еда🍛"),
            KeyboardButton(text= "🍻Напитки🍻"),
        ],
        [
            KeyboardButton(text="🥞Сладость🥞"),
            KeyboardButton(text="🍔Фастфоод🍔"),
            KeyboardButton(text="🍜Дешевая еда🍜")
        ]
    ],
    resize_keyboard=True
)