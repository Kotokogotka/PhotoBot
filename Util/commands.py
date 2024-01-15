from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_command(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запуск бота'
        ),
        BotCommand(
            command='help',
            description='Навигиция по боту'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())