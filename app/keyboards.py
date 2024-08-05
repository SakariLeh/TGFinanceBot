from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

use_functional_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Да'),
        KeyboardButton(text='Нет')
    ]
], resize_keyboard=True)

ER_choice_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Расходы', callback_data='Expense'),
        InlineKeyboardButton(text='Доходы', callback_data='Income'),
    ],
    [
        InlineKeyboardButton(text='Установить баланс', callback_data='set_balance'),
        InlineKeyboardButton(text='Получить совет', callback_data='get_advice')
    ],
    [
        InlineKeyboardButton(text='В главное меню', callback_data='Main_menu')
    ]
], resize_keyboard=True)

main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='В главное меню', callback_data='Main_menu')
    ]
])