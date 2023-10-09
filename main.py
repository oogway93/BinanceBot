import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: Message) -> Message:
    await message.answer(f"Hello my friend, {message.from_user.username}!")


@dp.message()
async def echo(message: Message) -> Message:
    await message.reply(text=f'{message.text}')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
