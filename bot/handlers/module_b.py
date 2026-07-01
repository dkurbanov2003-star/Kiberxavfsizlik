"""
module_b.py — Modul B: Tez yordam (SOS) va Kiber-Simulyator.

Ikki rejim:
  1) SOS — real hujum paytida bosqichma-bosqich harakat skripti:
       Shantaj / Bulling / Akkaunt(fishing) zanjirlari.
  2) Simulyator — xavfsiz mashq: 3 keys, to'g'ri javobga rag'bat,
       xatoga psixologik tuzoq izohi.

Texnik eslatma: bloklar orasida kichik kechikish (delay) qo'yamiz —
foydalanuvchi hamma tugmani birdan bosib yubormasligi va matnni
o'qishga ulgurishi uchun.
"""

import asyncio

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.keyboards.inline import (
    ak_2fa_kb,
    ak_pass_kb,
    ak_report_kb,
    ak_start_kb,
    bl_facts_kb,
    bl_noresp_kb,
    bl_shield_kb,
    bl_start_kb,
    legal_end_kb,
    module_b_kb,
    sh_block_kb,
    sh_evidence_kb,
    sh_money_kb,
    sh_start_kb,
    sim_next_kb,
    sim_options_kb,
    sos_menu_kb,
)
from bot.texts import messages as msg
from bot.texts.questions import SIMULATOR

router = Router()

DELAY_SECONDS = 1.5  # bloklar orasidagi kechikish


async def _edit(callback: CallbackQuery, text: str, keyboard, delay: bool = False) -> None:
    """Xabarni yangilaydi. delay=True bo'lsa, avval kichik pauza qiladi."""
    if delay:
        await callback.answer()  # tugmadagi "soat" belgisini o'chiramiz
        await asyncio.sleep(DELAY_SECONDS)
    await callback.message.edit_text(text, reply_markup=keyboard)
    if not delay:
        await callback.answer()


# ============================================================
#  MODUL B KIRISH
# ============================================================

@router.callback_query(F.data == "menu:b")
async def module_b_entry(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await _edit(callback, msg.SIM_OR_SOS, module_b_kb())


@router.callback_query(F.data == "b:sos")
async def sos_menu(callback: CallbackQuery) -> None:
    await _edit(callback, msg.SOS_MENU, sos_menu_kb())


# ============================================================
#  SHANTAJ ZANJIRI
# ============================================================

@router.callback_query(F.data == "sos:shantaj")
async def sh_start(callback: CallbackQuery) -> None:
    await _edit(callback, msg.SH_START, sh_start_kb(), delay=True)


@router.callback_query(F.data == "sh:money")
async def sh_money(callback: CallbackQuery) -> None:
    await _edit(callback, msg.SH_NO_MONEY, sh_money_kb())


@router.callback_query(F.data == "sh:evidence")
async def sh_evidence(callback: CallbackQuery) -> None:
    await _edit(callback, msg.SH_EVIDENCE, sh_evidence_kb())


@router.callback_query(F.data == "sh:block")
async def sh_block(callback: CallbackQuery) -> None:
    await _edit(callback, msg.SH_BLOCK, sh_block_kb())


@router.callback_query(F.data == "sh:legal")
async def sh_legal(callback: CallbackQuery) -> None:
    await _edit(callback, msg.SH_LEGAL, legal_end_kb(with_psychologist=False))


# ============================================================
#  BULLING ZANJIRI
# ============================================================

@router.callback_query(F.data == "sos:bulling")
async def bl_start(callback: CallbackQuery) -> None:
    await _edit(callback, msg.BL_START, bl_start_kb(), delay=True)


@router.callback_query(F.data == "bl:noresp")
async def bl_noresp(callback: CallbackQuery) -> None:
    await _edit(callback, msg.BL_NO_RESPONSE, bl_noresp_kb())


@router.callback_query(F.data == "bl:facts")
async def bl_facts(callback: CallbackQuery) -> None:
    await _edit(callback, msg.BL_COLLECT_FACTS, bl_facts_kb())


@router.callback_query(F.data == "bl:shield")
async def bl_shield(callback: CallbackQuery) -> None:
    await _edit(callback, msg.BL_SHIELD, bl_shield_kb())


@router.callback_query(F.data == "bl:legal")
async def bl_legal(callback: CallbackQuery) -> None:
    await _edit(callback, msg.BL_LEGAL, legal_end_kb(with_psychologist=True))


# ============================================================
#  AKKAUNT / FISHING ZANJIRI
# ============================================================

@router.callback_query(F.data == "sos:akkaunt")
async def ak_start(callback: CallbackQuery) -> None:
    await _edit(callback, msg.AK_START, ak_start_kb(), delay=True)


@router.callback_query(F.data == "ak:pass")
async def ak_pass(callback: CallbackQuery) -> None:
    await _edit(callback, msg.AK_PASSWORD, ak_pass_kb())


@router.callback_query(F.data == "ak:2fa")
async def ak_2fa(callback: CallbackQuery) -> None:
    await _edit(callback, msg.AK_2FA, ak_2fa_kb())


@router.callback_query(F.data == "ak:report")
async def ak_report(callback: CallbackQuery) -> None:
    await _edit(callback, msg.AK_REPORT, ak_report_kb())


@router.callback_query(F.data == "ak:legal")
async def ak_legal(callback: CallbackQuery) -> None:
    await _edit(callback, msg.AK_LEGAL, legal_end_kb(with_psychologist=False))


# ============================================================
#  KIBER-SIMULYATOR
# ============================================================

async def _show_case(callback: CallbackQuery, case_index: int) -> None:
    """Berilgan keysni variant tugmalari bilan chiqaradi."""
    scenario = SIMULATOR[case_index]["scenario"]
    await callback.message.edit_text(scenario, reply_markup=sim_options_kb(case_index))


@router.callback_query(F.data == "b:sim")
async def sim_start(callback: CallbackQuery) -> None:
    """Simulyatorni 1-keysdan boshlaydi."""
    await _show_case(callback, case_index=0)
    await callback.answer()


@router.callback_query(F.data.startswith("simnext:"))
async def sim_next(callback: CallbackQuery) -> None:
    """Keyingi keysga o'tadi."""
    next_index = int(callback.data.split(":", 1)[1])
    await _show_case(callback, case_index=next_index)
    await callback.answer()


@router.callback_query(F.data.startswith("simans:"))
async def sim_answer(callback: CallbackQuery) -> None:
    """Javobni baholaydi: to'g'ri/xato bo'yicha izoh beradi."""
    _, case_str, option_str = callback.data.split(":")
    case_index = int(case_str)
    option_index = int(option_str)

    option = SIMULATOR[case_index]["options"][option_index]
    feedback = option["feedback"]
    next_index = case_index + 1

    await callback.message.edit_text(feedback, reply_markup=sim_next_kb(next_index))
    await callback.answer("To'g'ri! 🎉" if option["correct"] else "Keling, tahlil qilamiz 🤔")
