import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

import config

from handlers import router 



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

if __name__ == "__main__" :
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    




