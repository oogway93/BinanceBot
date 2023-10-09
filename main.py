import asyncio

import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from BinanceAPI import url
from config import TOKEN
from handlers.handlers import router

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message) -> Message:
    await message.answer(f"Hello my friend, {message.from_user.username}!")


# @dp.message()
# async def echo(message: Message) -> Message:
#     await message.reply(text=f'{message.text}')
@dp.message()
async def get_price_handler(message: Message) -> Message:
    data = requests.get(f"{url}/ticker/price?symbol={message.text.upper().strip()}")
    json = data.json()
    await message.answer(f"{json['symbol']}: {json['price']}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
