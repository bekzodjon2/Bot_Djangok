from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Arzon_taomlar_uchun = ReplyKeyboardMarkup(
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
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)