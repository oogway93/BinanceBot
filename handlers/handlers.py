from aiogram import Router, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message, CallbackQuery
import httpx

import keyboard.ReplyKeyboards
from BinanceAPI_URLS import url
import keyboard
from utils.utils import converter_currency

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> Message:
    await message.delete()
    await message.answer(
        "Hello, I'm a binance bot! I can exchange currency, get shares, currency rate online and so on...",
        reply_markup=keyboard.ReplyKeyboards.main_kb)
    await message.answer('Look at below', reply_markup=keyboard.InlineKeyboards.docs)
    await message.answer_sticker("CAACAgQAAxkBAAEKgTllJumjWJ7_Xabx60lD-r87mVA7_QACUAEAAqghIQaxvfG1zemEojAE")


@router.callback_query()
async def callback_inline(call: CallbackQuery) -> CallbackQuery:
    with open("messages/msg.txt", encoding='utf-8') as f:
        msg = f.read()
        await call.answer(text=msg, show_alert=True)


@router.message(Command(commands=["assets"]))
async def crypto_assets_handler(message: Message, command: CommandObject) -> Message:
    data = httpx.get(url=f"{url}/ticker/price?symbol={command.args.upper().strip()}")
    if data.status_code == 200:
        json = data.json()
        exchange_data = converter_currency(amount=float(json['price']), from_cur='USD', to_cur='EUR')
        await message.answer(
            f"{json['symbol']}: {float(json['price'])}{exchange_data['old_currency']} | ~{exchange_data['new_amount']}{exchange_data['new_currency']}")
    else:
        await message.reply("<strong>Следуйте правилам, согласно документации!</strong>", parse_mode="HTML",
                            reply_markup=keyboard.InlineKeyboards.docs)


@router.message(Command(commands=["convert"]))
async def convert_currency_online_handler(message: Message, command: CommandObject) -> Message:
    command_args = command.args.rstrip().upper().split()
    conv_data = converter_currency(amount=command_args[0], from_cur=command_args[1], to_cur=command_args[2])
    await message.answer(
        f"{int(conv_data['old_amount'])} {conv_data['old_currency']} = ~{conv_data['new_amount']} {conv_data['new_currency']}")


@router.message(F.text == "About developer")
async def about_handler(message: Message) -> Message:
    with open("messages/about.txt", encoding='utf-8') as f:
        text = f.read()
        await message.answer(text, parse_mode="HTML", reply_markup=keyboard.InlineKeyboards.about_contacts)
