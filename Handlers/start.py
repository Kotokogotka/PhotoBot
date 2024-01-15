import os

from aiogram import Bot
from aiogram.types import Message
from Keyboards.register_kb import register_keyboard
from Keyboards.profile_kb import profile_kb
from Util.database import Database


async def get_start(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if (users):
        await bot.send_message(message.from_user.id,
                               f'Привет {users[1]}!', reply_markup=profile_kb)
    else:
        await bot.send_message(message.from_user.id, text='👋 Приветствую тебя друг!\n\n'
                                                          '🤖 Я бот-помощник Закатовой Кати 📸\n\n'
                                                          '🙎‍♀️ Ты наверняка уже с ней познакомилась, а теперь давай и я тебя узнаю лучше\n\n'
                                                          '📝 После знакомства передам всю информацию Кате и она постарается сделать вашу съемку незабываемой!',
                               reply_markup=register_keyboard)