from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
