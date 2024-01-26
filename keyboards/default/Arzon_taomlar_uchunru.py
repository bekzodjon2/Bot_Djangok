from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Arzon_taomlar_uchunru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Перашки"),
            KeyboardButton(text="Сомса")
        ],
        [
         KeyboardButton(text="Шашлык"),
         KeyboardButton(text="Нухат")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)