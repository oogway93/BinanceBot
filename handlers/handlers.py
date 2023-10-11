from aiogram import Router, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
import httpx

from BinanceAPI import url
from utils.utils import converter_currency

router = Router()


@router.message(Command(commands=["price"]))
async def get_price_handler(message: Message, command: CommandObject) -> Message:
    data = httpx.get(url=f"{url}/ticker/price?symbol={command.args.upper().strip()}")
    json = data.json()
    exchange_data = converter_currency(amount=float(json['price']), from_cur='USD', to_cur='EUR')
    await message.answer(
        f"{json['symbol']}: {float(json['price'])}$ | ~{exchange_data['new_amount']}руб.")


@router.message()
async def echo(message: Message) -> Message:
    await message.reply(text=f'{message.text}')
