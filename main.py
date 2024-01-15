import os

from aiogram import Bot, Dispatcher, F
import asyncio
from dotenv import load_dotenv

from Util.commands import set_command
from Handlers.start import get_start
from aiogram.filters import Command
from Handlers.register import start_register, register_phone, register_name
from State.register import Register_State

load_dotenv()

token = os.getenv('TOKEN')
admin_ids = os.getenv('ADMIN_IDS')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(admin_ids, text='Start bot')


dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))

# Хандлер для регистрации
dp.message.register(start_register, F.text=='Зарегистрироваться')
dp.message.register(register_name, Register_State.regname)
dp.message.register(register_phone, Register_State.regphone)

async def start():
    await set_command(bot)
    try:
        await dp.start_polling(bot, skip_update=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
