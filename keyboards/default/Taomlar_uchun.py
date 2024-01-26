from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
taomlar_uchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Palov")
        ],
        [
         KeyboardButton(text="Lagmon"),
         KeyboardButton(text="Chuchvara")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)