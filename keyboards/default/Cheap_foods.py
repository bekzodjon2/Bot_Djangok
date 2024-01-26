from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Arzon_taomlar_uchuneng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Perashka"),
            KeyboardButton(text="Somsa")
        ],
        [
         KeyboardButton(text="shashlik"),
         KeyboardButton(text="No'xat")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)