from aiogram.fsm.state import StatesGroup, State

class Register_State(StatesGroup):
    regname = State()
    regphone = State()