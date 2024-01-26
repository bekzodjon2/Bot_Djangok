from loader import dp
from aiogram import types

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(text="Siz notog'ri buyruq yozdingliz")
