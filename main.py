import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.handlers import router

async def launch():
    bot = Bot(token=open('app/token.txt').read())
    disp = Dispatcher()
    disp.include_router(router)
    await disp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(launch())
    except KeyboardInterrupt:
        print('бот выключен')