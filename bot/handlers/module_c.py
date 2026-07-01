"""
module_c.py — Modul C: Konsultatsiya va mutaxassisga eskalatsiya.

Ikki bosqichli model:
  1) Tahdid turini tanlash (shantaj / bulling / firibgarlik).
  2) Tayyor PSIXOLOGIK + YURIDIK konsultatsiya bir xabarda.
  3) "Javob topmadim" -> anonim aloqa oynasi. Foydalanuvchi xabar/audio
     yozadi; profili KO'RINMAYDI, faqat maxfiy raqam beriladi.

Agar .env da ADMIN_CHAT_ID sozlangan bo'lsa, anonim murojaat o'sha
mutaxassis chatiga yuboriladi (yuboruvchi shaxsi oshkor qilinmaydi).
"""

import secrets

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.config import load_config
from bot.keyboards.inline import back_to_menu_kb, consult_kb, module_c_kb
from bot.states.user_states import SupportStates
from bot.texts import messages as msg

router = Router()
_config = load_config()

# Tanlangan mavzuga mos konsultatsiya matni
_CONSULT_TEXTS = {
    "shantaj": msg.C_SHANTAJ,
    "bulling": msg.C_BULLING,
    "fraud": msg.C_FRAUD,
}


@router.callback_query(F.data == "menu:c")
async def module_c_entry(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.edit_text(msg.C_MENU, reply_markup=module_c_kb())
    await callback.answer()


@router.callback_query(F.data.startswith("c:"))
async def show_consultation(callback: CallbackQuery) -> None:
    """Tanlangan mavzu bo'yicha psixologik+yuridik konsultatsiyani chiqaradi."""
    topic = callback.data.split(":", 1)[1]
    text = _CONSULT_TEXTS.get(topic)
    if text is None:
        await callback.answer("Noma'lum mavzu", show_alert=True)
        return
    await callback.message.edit_text(text, reply_markup=consult_kb())
    await callback.answer()


@router.callback_query(F.data == "cchat:start")
async def start_anon_chat(callback: CallbackQuery, state: FSMContext) -> None:
    """Anonim aloqa oynasini ochadi va maxfiy raqam beradi."""
    code = f"M-{secrets.randbelow(90000) + 10000}"  # masalan M-48213
    await state.set_state(SupportStates.waiting_message)
    await state.update_data(secret_code=code)
    await callback.message.edit_text(msg.C_ANON_CHAT_START.format(code=code))
    await callback.answer()


@router.message(SupportStates.waiting_message)
async def receive_anon_message(message: Message, state: FSMContext) -> None:
    """Foydalanuvchi anonim murojaatini qabul qiladi va (sozlangan bo'lsa) uzatadi."""
    data = await state.get_data()
    code = data.get("secret_code", "M-00000")
    await state.clear()

    # Agar mutaxassis chati sozlangan bo'lsa — xabarni ANONIM uzatamiz.
    # Diqqat: forward EMAS (u profilni oshkor qiladi), balki copy_to ishlatamiz.
    if _config.admin_chat_id is not None:
        try:
            await message.bot.send_message(
                chat_id=_config.admin_chat_id,
                text=f"📩 <b>Yangi anonim murojaat</b>\nMaxfiy raqam: <b>{code}</b>",
            )
            await message.copy_to(chat_id=_config.admin_chat_id)
        except Exception:
            # Mutaxassis chatiga yuborib bo'lmasa ham, foydalanuvchi xabarini yo'qotmaymiz
            pass

    await message.answer(
        msg.C_ANON_CHAT_SAVED.format(code=code),
        reply_markup=back_to_menu_kb(),
    )
