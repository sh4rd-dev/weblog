import requests
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.filters.callback_data import CallbackData
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

import config
from loader import bot


class botCallback(CallbackData, prefix="call"):
    action: str

class newPost(StatesGroup):
    start = State()
    title = State()
    text = State()

handler = Router()

@handler.message(Command(commands=['start']))
async def start_bot(message: Message, state: FSMContext):
    await message.answer(text='<b>Выберите кнопку:</b>', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Выставить новый пост', callback_data='addNewPost'),
        ]
    ]))
    await state.set_data(newPost.start)

@handler.callback_query(newPost.start)
async def addNewPostTitle(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text='<b>Введите название статьи:</b>')
    await state.set_state(newPost.title)

@handler.message(newPost.title)
async def addNewPostText(message: Message, state: FSMContext):
    await message.answer(text="<b>Введите текст статьи:</b>")
    await state.update_data(title=message.text)
    await state.set_state(newPost.text)

@handler.message(newPost.text)
async def addNewPostText(message: Message, state: FSMContext):
    await message.answer(text='Статья успешно создана на сайте!')
    title = await state.get_data()['title']
    await state.clear()
    requests.post(config.domain, {"action": "addNewPost", "data": {"title": title, "text": message.text}})
    