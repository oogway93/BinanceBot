import requests
from aiogram import Router, Dispatcher
from aiogram.types import Message

from BinanceAPI import url

router = Router()


# @router.message()
async def get_price_handler(message: Message) -> Message:
    data = requests.get(f"{url}/ticker/price?symbol={message.text.upper().strip()}")
    await message.answer(f"{data[1]}")


# def register_handlers(dp: Dispatcher):
#     dp.(get_price_handler)
