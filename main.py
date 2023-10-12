import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import handlers.handlers
from config import TOKEN
from keyboard.keyboard import main_kb

bot = Bot(TOKEN)
dp = Dispatcher()




async def main():
    dp.include_router(
        handlers.handlers.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
