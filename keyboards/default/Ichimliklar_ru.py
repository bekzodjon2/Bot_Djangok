from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Ichimliklar_uchun_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пепси"),
            KeyboardButton(text="Кола")
        ],
        [
            KeyboardButton(text="Фанта"),
            KeyboardButton(text="Чай"),
            KeyboardButton(text="Кофе")

        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)