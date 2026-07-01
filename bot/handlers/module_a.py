"""
module_a.py — Modul A: Diagnostika (Kiber-Resilyentlik testi).

Algoritm (topshiriqqa muvofiq):
  - Har safar faqat 1 savol + 3 tugma chiqadi; javob berilsa savol yangilanadi.
  - Ballar yashirin hisoblanadi (A=1, B=2, C=3), FSM ichida to'planadi.
  - Oxirgi savoldan keyin ball SPSS uchun Excel'ga yoziladi.
  - Natija rag'batlantiruvchi tilda ko'rsatiladi.

Ball shkalasi: 9 savol x (1..3) = 9..27 ball.
  9–15  -> Yuqori xavf guruhi (risk)
  16–22 -> O'rta (barqaror) guruh (middle)
  23–27 -> Yuqori kiber-immunitet (high)
"""

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.config import load_config
from bot.database.storage import save_result
from bot.keyboards.inline import question_kb, result_kb
from bot.states.user_states import TestStates
from bot.texts import messages as msg
from bot.texts.questions import QUESTIONS

router = Router()
_config = load_config()


async def _show_question(callback: CallbackQuery, index: int) -> None:
    """Berilgan indeksdagi savolni chiqaradi (raqamlangan holda)."""
    question = QUESTIONS[index]
    text = (
        f"🧪 <b>Savol {index + 1}/{len(QUESTIONS)}</b>\n\n"
        f"{question['text']}"
    )
    await callback.message.edit_text(text, reply_markup=question_kb(index))


@router.callback_query(F.data == "menu:a")
async def start_test(callback: CallbackQuery, state: FSMContext) -> None:
    """Testni boshlaydi: hisoblagichlarni nolga qo'yadi va 1-savolni chiqaradi."""
    await state.set_state(TestStates.answering)
    await state.update_data(index=0, score=0)
    await _show_question(callback, index=0)
    await callback.answer()


@router.callback_query(TestStates.answering, F.data.startswith("test_ans:"))
async def on_answer(callback: CallbackQuery, state: FSMContext) -> None:
    """Javob bosilganda: ballni qo'shadi va keyingi savolga o'tadi yoki yakunlaydi."""
    points = int(callback.data.split(":", 1)[1])
    data = await state.get_data()
    index = data["index"] + 1
    score = data["score"] + points

    if index < len(QUESTIONS):
        # Yana savol bor — keyingisini ko'rsatamiz
        await state.update_data(index=index, score=score)
        await _show_question(callback, index=index)
        await callback.answer()
        return

    # Test tugadi — ballni bazaga yozamiz va natijani chiqaramiz
    await state.clear()
    await save_result(
        telegram_id=callback.from_user.id,
        score=score,
        excel_path=_config.excel_path,
    )
    await _show_result(callback, score)
    await callback.answer("Test yakunlandi ✅")


async def _show_result(callback: CallbackQuery, score: int) -> None:
    """Ballga qarab mos natija matnini va keyingi qadam tugmasini chiqaradi."""
    if score <= 15:
        text, level = msg.RESULT_HIGH_RISK, "risk"
    elif score <= 22:
        text, level = msg.RESULT_MIDDLE, "middle"
    else:
        text, level = msg.RESULT_HIGH_IMMUNITY, "high"

    await callback.message.edit_text(
        text.format(score=score),
        reply_markup=result_kb(level),
    )
