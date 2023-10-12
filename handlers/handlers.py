from aiogram import Router
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message, CallbackQuery
import httpx

from BinanceAPI import url
from keyboard.keyboard import main_kb, docs
from utils.utils import converter_currency

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> Message:
    await message.delete()
    await message.answer(
        f"Hello, I'm a binance bot! I can exchange currency, get shares, currency rate online and so on...",
        reply_markup=main_kb)
    await message.answer('Look at below', reply_markup=docs)
    await message.answer_sticker("CAACAgQAAxkBAAEKgTllJumjWJ7_Xabx60lD-r87mVA7_QACUAEAAqghIQaxvfG1zemEojAE")


@router.callback_query()
async def callback_inline(call: CallbackQuery):
    with open("msg.txt", encoding='utf-8') as f:
        msg = f.read()
        await call.answer(text=msg, show_alert=True)


@router.message(Command(commands=["assets"]))
async def crypto_assets_handler(message: Message, command: CommandObject) -> Message:
    data = httpx.get(url=f"{url}/ticker/price?symbol={command.args.upper().strip()}")
    json = data.json()
    exchange_data = converter_currency(amount=float(json['price']), from_cur='USD', to_cur='EUR')
    await message.answer(
        f"{json['symbol']}: {float(json['price'])}$ | ~{exchange_data['new_amount']}{exchange_data['new_currency']}")


@router.message(Command(commands=["convert"]))
async def convert_currency_online_handler(message: Message, command: CommandObject) -> Message:
    command_args = command.args.rstrip().upper().split()
    conv_data = converter_currency(amount=command_args[0], from_cur=command_args[1], to_cur=command_args[2])
    await message.answer(
        f"{int(conv_data['old_amount'])} {conv_data['old_currency']} = ~{conv_data['new_amount']} {conv_data['new_currency']}")


