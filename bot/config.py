"""
config.py — Botning markaziy sozlamalari.

Bu fayl maxfiy tokenni .env faylidan xavfsiz o'qib oladi.
Token hech qachon kod ichida ochiq yozilmaydi!
"""

from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os

# Loyihaning asosiy papkasi (ildiz)
BASE_DIR = Path(__file__).resolve().parent.parent

# .env faylini yuklaymiz (ichida BOT_TOKEN bor)
load_dotenv(BASE_DIR / ".env")


@dataclass
class Config:
    """Botning barcha sozlamalari shu yerda jamlanadi."""

    bot_token: str

    # Anonim xabarlar yuboriladigan mutaxassis/admin chat ID'si (ixtiyoriy).
    # Agar berilmasa, xabarlar faqat serverda saqlanadi.
    admin_chat_id: int | None = None

    # Ma'lumotlar (SPSS uchun) yoziladigan Excel fayl manzili
    excel_path: Path = BASE_DIR / "malumotlar.xlsx"


def load_config() -> Config:
    """.env dan sozlamalarni o'qib, Config obyektini qaytaradi."""
    token = os.getenv("BOT_TOKEN")

    if not token or token.startswith("1234567890"):
        raise ValueError(
            "❌ BOT_TOKEN topilmadi yoki namuna qiymat qolib ketgan!\n"
            "   .env faylini yarating va BotFather'dan olgan tokeningizni qo'ying.\n"
            "   Namuna: cp .env.example .env"
        )

    # admin_chat_id ixtiyoriy — bo'sh bo'lsa None qoladi
    admin_raw = os.getenv("ADMIN_CHAT_ID", "").strip()
    admin_chat_id = int(admin_raw) if admin_raw.lstrip("-").isdigit() else None

    return Config(bot_token=token, admin_chat_id=admin_chat_id)
