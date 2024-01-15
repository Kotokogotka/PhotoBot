import re

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from State.register import Register_State
import os
from Util.database import Database


async def start_register(message: Message, state: FSMContext):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if(users):
        await message.answer(f'{users[1]}\n Ты уже зарегестрирована')
    else:
        await message.answer(f'Рада, что ты решилась!\n\n'
                             'Скажи, как тебя зовут?'
                             )
        await state.set_state(Register_State.regname)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Приятно познакомиться {message.text}\n\n'
                         f'Теперь укажи свой номер телефона 📱\n'
                         f'Формат телефона: +7хххххххххх\n\n'
                         f'⚠ Внимание! Я чувствителен к формату ввода номера')
    await state.update_data(regname=message.text)
    await state.set_state(Register_State.regphone)


async def register_phone(message: Message, state: FSMContext):
    if (re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)
        red_data = await state.update_data()
        reg_name = red_data.get('regname')
        reg_phone = red_data.get('regphone')
        await message.answer(
            text=f'Приятно познакомиться {reg_name}\n\n'
                 f'Номер телефона {reg_phone}'
        )
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, telegram_id=message.from_user.id)
        await state.clear()

    else:
        await message.answer(
            text='Номер телефона введен не правильно!'
        )
