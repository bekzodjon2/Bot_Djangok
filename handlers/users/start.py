from aiogram.types import CallbackQuery
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.Arzon_taomlar_uchunru import Arzon_taomlar_uchunru
from keyboards.default.Fast_food_ru import Fastfood_uchunru
from keyboards.default.Ichimliklar_ru import Ichimliklar_uchun_ru
from keyboards.default.Orqaga_ru import Orqaga_uchun_ru
from keyboards.default.Shirinliklar_ru import Shirinliklar_uchun_ru
from keyboards.default.Taomlar_ru import taomlar_uchun_ru
from keyboards.default.bot_button import menu_uchun
from keyboards.default.Taomlar_uchun import taomlar_uchun
from keyboards.default.Ichimliklar_uchun import Ichimliklar_uchun
from keyboards.default.Shirinliklar_uchun import Shirinliklar_uchun
from keyboards.default.Fast_food_uchun import Fastfood_uchun
from keyboards.default.Arzon_taomlar import Arzon_taomlar_uchun
from keyboards.default.Orqaga_buttons import Orqaga
from loader import dp
from keyboards.inline.inline_button import tillar_button
from keyboards.default.Menu2eng import menu_uchun2eng
from keyboards.default.Meals_eng import taomlar_uchuneng
from keyboards.default.Drinks import Ichimliklar_uchuneng
from keyboards.default.Sweets import Shirinliklar_uchuneng
from keyboards.default.Fast_food_eng import Fastfood_uchuneng
from keyboards.default.Cheap_foods import Arzon_taomlar_uchuneng
from keyboards.default.Orqaga2eng import Menu_back
from keyboards.default.Menu_rus import menu_uchun_ru

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum : {message.from_user.full_name}! Botimizga hush kelibsiz",reply_markup=tillar_button)

@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum botga hush kelibsiz",reply_markup=menu_uchun)

@dp.message_handler(text="🍛Taomlar🍛")
async def bot_start(message: types.Message):
    await message.answer(f"Siz Taomlar Taomlar menusidasiz",reply_markup=taomlar_uchun)

@dp.message_handler(text="🍻Ichimliklar🍻")
async def bot_start(message: types.Message):
    await message.answer(f"Siz Ichimliklar menusidasiz",reply_markup=Ichimliklar_uchun)

@dp.message_handler(text="🥞Shirinliklar🥞")
async def bot_start(message: types.Message):
    await message.answer(f"Siz Shirinliklar menusidasiz",reply_markup=Shirinliklar_uchun)

@dp.message_handler(text="🍔Fast food🍔")
async def bot_start(message: types.Message):
    await message.answer(f"Siz Fast food menusidasiz",reply_markup=Fastfood_uchun)

@dp.message_handler(text="🍜Arzon taomlar🍜")
async def bot_start(message: types.Message):
    await message.answer(f"Siz Arzon taomlar menusidasiz",reply_markup=Arzon_taomlar_uchun)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum siz Asosiy menyudasiz",reply_markup=Orqaga)

# ingliz tili uchun

@dp.callback_query_handler(text="til2")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Hello {xabar.from_user.full_name} welcome bot ",reply_markup=menu_uchun2eng)

@dp.message_handler(text="🍛Meals🍛")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Meals :",reply_markup=taomlar_uchuneng)

@dp.message_handler(text="🍻Drinks🍻")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Drinks :",reply_markup=Ichimliklar_uchuneng)

@dp.message_handler(text="🥞Sweets🥞")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Sweets :",reply_markup=Shirinliklar_uchuneng)

@dp.message_handler(text="🍔Fastfood🍔")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Fast food :",reply_markup=Fastfood_uchuneng)

@dp.message_handler(text="🍜Cheap foods🍜")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Cheap foods :",reply_markup=Arzon_taomlar_uchuneng)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"You back Menu",reply_markup=Menu_back)
# Rus tili uchun

@dp.callback_query_handler(text="til3")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Привет {xabar.from_user.full_name} добро пожаловать в бот ",reply_markup=menu_uchun_ru)

@dp.message_handler(text="🍛Еда🍛")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Meals :",reply_markup=taomlar_uchun_ru)
@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"You back Menu",reply_markup=Orqaga_uchun_ru)

@dp.message_handler(text="🍻Напитки🍻")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Drinks :",reply_markup=Ichimliklar_uchun_ru)
@dp.message_handler(text="🥞Сладость🥞")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Sweets :",reply_markup=Shirinliklar_uchun_ru)

@dp.message_handler(text="🍔Фастфоод🍔")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Fast food :",reply_markup=Fastfood_uchunru)

@dp.message_handler(text="🍜Дешевая еда🍜")
async def bot_start(message: types.Message):
    await message.answer(f"Choice Cheap foods :",reply_markup=Arzon_taomlar_uchunru)















































