from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
taomlar_uchun_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Плов"),
            KeyboardButton(text="Жареная рыба")
        ],
        [
         KeyboardButton(text="Гриль"),
         KeyboardButton(text="Пельмени")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)