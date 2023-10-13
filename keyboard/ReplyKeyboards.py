from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
