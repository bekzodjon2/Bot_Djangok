from aiogram import types
from googletrans import Translator
from loader import dp
tarjimon = Translator()


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    til  = tarjimon.detect(text=message.text).lang
    if til=='uz':
        tarjima_qilish = tarjimon.translate(text=message.text,dest='en',src='uz').text
        await message.answer(text=tarjima_qilish)