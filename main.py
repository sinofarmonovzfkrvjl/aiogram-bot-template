import asyncio
from aiogram import Dispatcher
from utils import bot, storage, router, set_commands
from handlers import register_all_handlers
import logging

async def main():
    dp = Dispatcher(storage=storage)

    dp.include_router(router)

    register_all_handlers(router)

    await set_commands(bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())