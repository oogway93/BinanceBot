import asyncio

from aiogram import Bot, Dispatcher

import handlers.handlers
from config import TOKEN

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
