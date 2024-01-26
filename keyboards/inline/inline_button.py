from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

tillar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili🇺🇿",callback_data="til1"),
            InlineKeyboardButton(text="Ingliz tili🇺🇸",callback_data="til2")

        ],
        [
            InlineKeyboardButton(text="Rus tili🇷🇺",callback_data="til3")
        ]
    ]
)
