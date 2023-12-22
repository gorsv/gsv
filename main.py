from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

import config
from handlers import Gen, kb, utils, parse, rest  # Подключение ваших модулей


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.callback_query_handler(lambda query: query.data == "generate_rasp")
async def generate_rasp_callback(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Давайте начнем! Ответьте на несколько вопросов для составления расписания.")
    await Gen.text_prompt.set()

@dp.message_handler(state=Gen.text_prompt)
async def generate_schedule_handler(message: types.Message, state: FSMContext):
    user_response = message.text
    df_parse = parse.handle_text(user_response)
    df_rest = rest.input_data()
    schedule_text = await utils.generate_schedule(df_parse, df_rest)
    await message.answer(f"Ваше расписание на день:\n{schedule_text}")
    await state.finish()

async def main(): 
    try:
        bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
        dp = Dispatcher(storage=MemoryStorage())
        dp.message.middleware(ChatActionMiddleware())
        dp.include_router(router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logging.error(f"Ошибка(): {e}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
    
