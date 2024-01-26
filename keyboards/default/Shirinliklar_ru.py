from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Shirinliklar_uchun_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Печенье с шоколадной крошкой"),
            KeyboardButton(text="Конфеты палочки")
        ],
        [
            KeyboardButton(text="Торт"),
            KeyboardButton(text="Шоколодное морожное"),
            KeyboardButton(text="Шоколодное Масло")

        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)