import asyncio
import logging
import betterlogging as bl


logger = logging.getLogger(__name__)
bl.basic_colorized_config(level=logging.INFO)

async def start_web_server():
    pass

# Главная функция, через которую мы запускаем весь проект.
async def main():
    from loader import bot, dp

    from handlers import handlers
    dp.include_routers(handlers.handlers)
    

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())