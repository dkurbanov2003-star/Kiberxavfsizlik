"""
inline.py — Inline (xabar ostidagi) tugmalar to'plami.

Har bir tugmada "callback_data" bor — foydalanuvchi bosganda botga
yuboriladigan yashirin signal. Handler shu signalni ushlab, kerakli
javobni beradi. Barcha signal nomlari shu yerda markazlashtirilgan.
"""

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.texts.questions import QUESTIONS, SIMULATOR


# ============================================================
#  /start ZANJIRI
# ============================================================

def start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🚀 Boshlash", callback_data="reg:start")
    return kb.as_markup()


def gender_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="👦 Yigit", callback_data="reg_gender:Yigit")
    kb.button(text="👧 Qiz", callback_data="reg_gender:Qiz")
    return kb.as_markup()


def age_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="11-13 yosh", callback_data="reg_age:11-13")
    kb.button(text="14-15 yosh", callback_data="reg_age:14-15")
    kb.button(text="16-17 yosh", callback_data="reg_age:16-17")
    kb.adjust(3)
    return kb.as_markup()


def main_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🧪 Kiber-Resilyentlikni tekshirish (Test)", callback_data="menu:a")
    kb.button(text="🚨 Tez yordam: Menga hujum qilishyapti!", callback_data="menu:b")
    kb.button(text="💬 Psixolog bilan anonim chat", callback_data="menu:c")
    kb.adjust(1)  # har bir tugma alohida qatorda
    return kb.as_markup()


# ============================================================
#  MODUL A — TEST
# ============================================================

def question_kb(index: int) -> InlineKeyboardMarkup:
    """Berilgan savol uchun 3 ta variant tugmasi (ballari bilan)."""
    kb = InlineKeyboardBuilder()
    for text, points in QUESTIONS[index]["options"]:
        kb.button(text=text, callback_data=f"test_ans:{points}")
    kb.adjust(1)
    return kb.as_markup()


def result_kb(level: str) -> InlineKeyboardMarkup:
    """Test natijasiga qarab keyingi qadam tugmalari."""
    kb = InlineKeyboardBuilder()
    if level == "risk":
        kb.button(text="🛡 Tez yordam: Himoya usullari", callback_data="menu:b")
    elif level == "middle":
        kb.button(text="🎮 Kiber-Keyslar Simulyatori", callback_data="b:sim")
    else:  # high immunity
        kb.button(text="💬 Anonim maslahat portali", callback_data="menu:c")
    kb.button(text="🏠 Bosh menyu", callback_data="menu:main")
    kb.adjust(1)
    return kb.as_markup()


# ============================================================
#  MODUL B — SOS va SIMULYATOR
# ============================================================

def module_b_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🚨 SOS: Menga hozir hujum qilishyapti", callback_data="b:sos")
    kb.button(text="🎮 Kiber-Simulyator (mashq)", callback_data="b:sim")
    kb.button(text="🏠 Bosh menyu", callback_data="menu:main")
    kb.adjust(1)
    return kb.as_markup()


def sos_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🔒 Shaxsiy rasm/sirlar bilan qo'rqitishyapti (Shantaj)", callback_data="sos:shantaj")
    kb.button(text="💢 Guruhlarda haqorat qilishyapti (Bulling)", callback_data="sos:bulling")
    kb.button(text="⚠️ Akkauntimni o'g'irlashdi / Shubhali ssilka", callback_data="sos:akkaunt")
    kb.button(text="🏠 Bosh menyu", callback_data="menu:main")
    kb.adjust(1)
    return kb.as_markup()


# --- Shantaj zanjiri tugmalari ---
def sh_start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="1️⃣ Pul o'tkazmaslik!", callback_data="sh:money")
    kb.button(text="2️⃣ Dalillarni saqlash!", callback_data="sh:evidence")
    kb.button(text="3️⃣ Aloqani uzish!", callback_data="sh:block")
    kb.adjust(1)
    return kb.as_markup()


def sh_money_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="2️⃣ Dalillarni saqlash", callback_data="sh:evidence")
    kb.button(text="⬅️ Orqaga", callback_data="sos:shantaj")
    kb.adjust(1)
    return kb.as_markup()


def sh_evidence_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="3️⃣ Aloqani uzish", callback_data="sh:block")
    kb.button(text="⬅️ Orqaga", callback_data="sos:shantaj")
    kb.adjust(1)
    return kb.as_markup()


def sh_block_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="⚖️ Huquqiy va ijtimoiy yordam", callback_data="sh:legal")
    kb.adjust(1)
    return kb.as_markup()


# --- Bulling zanjiri tugmalari ---
def bl_start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="1️⃣ Javob qaytarmaslik!", callback_data="bl:noresp")
    kb.button(text="2️⃣ Faktlarni yig'ish!", callback_data="bl:facts")
    kb.button(text="3️⃣ Raqamli qalqon!", callback_data="bl:shield")
    kb.adjust(1)
    return kb.as_markup()


def bl_noresp_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="2️⃣ Faktlarni yig'ish", callback_data="bl:facts")
    kb.button(text="⬅️ Orqaga", callback_data="sos:bulling")
    kb.adjust(1)
    return kb.as_markup()


def bl_facts_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="3️⃣ Raqamli qalqon", callback_data="bl:shield")
    kb.button(text="⬅️ Orqaga", callback_data="sos:bulling")
    kb.adjust(1)
    return kb.as_markup()


def bl_shield_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="⚖️ Huquqiy va ijtimoiy choralar", callback_data="bl:legal")
    kb.adjust(1)
    return kb.as_markup()


# --- Akkaunt/fishing zanjiri tugmalari ---
def ak_start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="1️⃣ Parolni o'zgartirish!", callback_data="ak:pass")
    kb.button(text="2️⃣ Ikki bosqichli himoya!", callback_data="ak:2fa")
    kb.button(text="3️⃣ Ogohlantirish va xabar!", callback_data="ak:report")
    kb.adjust(1)
    return kb.as_markup()


def ak_pass_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="2️⃣ Ikki bosqichli himoya", callback_data="ak:2fa")
    kb.button(text="⬅️ Orqaga", callback_data="sos:akkaunt")
    kb.adjust(1)
    return kb.as_markup()


def ak_2fa_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="3️⃣ Ogohlantirish va xabar", callback_data="ak:report")
    kb.button(text="⬅️ Orqaga", callback_data="sos:akkaunt")
    kb.adjust(1)
    return kb.as_markup()


def ak_report_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="⚖️ Huquqiy va texnik choralar", callback_data="ak:legal")
    kb.adjust(1)
    return kb.as_markup()


def legal_end_kb(with_psychologist: bool = False) -> InlineKeyboardMarkup:
    """SOS zanjiri oxiridagi umumiy navigatsiya tugmalari."""
    kb = InlineKeyboardBuilder()
    kb.button(text="🧪 Kiber-Resilyentlikni tekshirish (Test)", callback_data="menu:a")
    if with_psychologist:
        kb.button(text="💬 Psixolog bilan anonim chat", callback_data="menu:c")
    else:
        kb.button(text="💬 Anonim maslahat portali", callback_data="menu:c")
    kb.button(text="🏠 Bosh menyuga qaytish", callback_data="menu:main")
    kb.adjust(1)
    return kb.as_markup()


# --- Simulyator tugmalari ---
def sim_options_kb(case_index: int) -> InlineKeyboardMarkup:
    """Berilgan keys uchun variant tugmalari: simans:<keys>:<variant>."""
    kb = InlineKeyboardBuilder()
    for option_index, option in enumerate(SIMULATOR[case_index]["options"]):
        kb.button(
            text=option["text"],
            callback_data=f"simans:{case_index}:{option_index}",
        )
    kb.adjust(1)
    return kb.as_markup()


def sim_next_kb(next_case_index: int) -> InlineKeyboardMarkup:
    """Javobdan keyin: keyingi keys yoki yakun."""
    kb = InlineKeyboardBuilder()
    if next_case_index < len(SIMULATOR):
        kb.button(text="➡️ Keyingi keys", callback_data=f"simnext:{next_case_index}")
    else:
        kb.button(text="🏠 Bosh menyu", callback_data="menu:main")
        kb.button(text="🚨 Tez yordam bo'limi", callback_data="menu:b")
    kb.adjust(1)
    return kb.as_markup()


# ============================================================
#  MODUL C — KONSULTATSIYA
# ============================================================

def module_c_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🔒 Kiber-shantaj bo'yicha konsultatsiya", callback_data="c:shantaj")
    kb.button(text="💢 Kiberbulling bo'yicha konsultatsiya", callback_data="c:bulling")
    kb.button(text="⚠️ Kiberfirbgarlik bo'yicha konsultatsiya", callback_data="c:fraud")
    kb.button(text="🏠 Bosh menyu", callback_data="menu:main")
    kb.adjust(1)
    return kb.as_markup()


def consult_kb() -> InlineKeyboardMarkup:
    """Konsultatsiya matni ostidagi eskalatsiya tugmasi."""
    kb = InlineKeyboardBuilder()
    kb.button(
        text="✍️ Savolimga javob topmadim (Mutaxassis bilan anonim aloqa)",
        callback_data="cchat:start",
    )
    kb.button(text="🏠 Bosh menyu", callback_data="menu:main")
    kb.adjust(1)
    return kb.as_markup()


def back_to_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🏠 Bosh menyu", callback_data="menu:main")
    return kb.as_markup()
