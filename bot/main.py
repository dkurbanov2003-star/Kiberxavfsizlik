"""
main.py — Botning ishga tushirish nuqtasi (entry point).

Bu yerda:
  - sozlamalar (token) o'qiladi;
  - Bot va Dispatcher yaratiladi (HTML rejim yoqiladi);
  - barcha modul routerlari (start, A, B, C) ulanadi;
  - ma'lumotlar bazasi (SQLite) tayyorlanadi;
  - polling (Telegram'dan xabarlarni tinglash) boshlanadi.

Ishga tushirish:  python -m bot.main
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import load_config
from bot.database.storage import init_db
from bot.handlers import module_a, module_b, module_c, start

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


async def main() -> None:
    config = load_config()

    # parse_mode=HTML => matnlardagi <b>...</b> teglari ishlaydi
    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # Modullarni ulaymiz (tartib muhim emas — filtrlar aniq)
    dp.include_router(start.router)
    dp.include_router(module_a.router)
    dp.include_router(module_b.router)
    dp.include_router(module_c.router)

    # Ma'lumotlar bazasini tayyorlaymiz
    await init_db()

    logger.info("Bot ishga tushmoqda...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot to'xtatildi.")
