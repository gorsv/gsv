from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    text_promt = State()
    img_promt = State()
