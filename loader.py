from aiogram import Dispatcher, Bot
from aiogram.fsm.strategy import FSMStrategy
from aiogram.fsm.storage.memory import MemoryStorage

# Все импорты с файлов бота
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)