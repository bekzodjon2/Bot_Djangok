from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Shirinliklar_uchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Shokoladli pechenye"),
            KeyboardButton(text="Shirin tayoqchalar")
        ],
        [
            KeyboardButton(text="To'rt"),
            KeyboardButton(text="Shokoladli muzqaymoq"),
            KeyboardButton(text="Keks")

        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)