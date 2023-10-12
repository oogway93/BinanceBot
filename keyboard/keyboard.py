from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            # KeyboardButton(text="/convert", ),
            # KeyboardButton(text="/asset")
            KeyboardButton(text="About developer")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие ниже",
    selective=True
)

docs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Docs", callback_data='docs')
        ]
    ]
)

about_contacts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='GitHub', url="https://github.com/oogway93")
        ]
    ]
)
