from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import CommandStart, Command

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import app.keyboards as kb



class Form(StatesGroup):
    name = State()
    use_functional = State()
    ER_choice = State()
    income1 = State()
    expense1 = State()
    income2 = State()
    expense2 = State()
    advice = State()



router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer('Привет, я бот. Назови своё имя', reply_markup=ReplyKeyboardRemove())


@router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.use_functional)
    await message.reply(f'Приятно познакомиться, {message.text}!\n'
                        f'Хотели бы вы воспользоваться нашим функционалом?', reply_markup=kb.use_functional_kb)


@router.message(Form.use_functional, F.text == 'Да')
async def func_response_yes(message: Message, state: FSMContext):
    await state.set_state(Form.ER_choice)
    await message.reply(f'Здорово, выберите функцию!\nКстати, сегодня на улице {34} градусов',
                        reply_markup=kb.ER_choice_kb)


@router.message(Form.use_functional, F.text == 'Нет')
async def func_response_no(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.reply('Очень жаль!\nЕсли понадоблюсь, пишите /start', reply_markup=ReplyKeyboardRemove())


@router.message(Form.use_functional, F.data == 'set_balance')
async def set_bal(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Form.use_functional)
    await callback.message.reply('Введите сумму на балансе')


@router.message(Form.use_functional, F.data == 'Income')
async def income_count(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Form.income1)
    await callback.message.edit_text('А теперь, введите сумму, которую стоит посчитать как доход',
                                     reply_markup=kb.main_menu_kb)


@router.callback_query(Form.use_functional, F.data == 'Expense')
async def expense_count(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Form.expense1)
    await callback.message.edit_text('А теперь, введите сумму, которую стоит посчитать как расход',
                                     reply_markup=kb.main_menu_kb)


@router.callback_query(Form.use_functional, F.data == 'get_advice')
async def advice(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Form.advice)

    await callback.message.edit_text()


@router.callback_query(Form.income1, F.text)
async def income_count2(callback: CallbackQuery, state: FSMContext):

    while True:
        try:
            int(F.text)
        except ValueError:
            await callback.message.answer('Ввод должен быть числовым')
        else:
            await callback.message.answer('Ваш доход был успешно сохранён',
                                     reply_markup=kb.main_menu_kb)
            await state.set_state(Form.use_functional)
            break


