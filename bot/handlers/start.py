"""
start.py — Boshlang'ich zanjir (/start) va umumiy navigatsiya.

Oqim:
  /start -> Xush kelibsiz + anonimlik kafolati (Boshlash tugmasi)
        -> Jins tanlash -> Yosh tanlash (Sotsiologik pasport)
        -> Bosh menyu (3 modul)

Bu router "menu:main" tugmasini ham boshqaradi (barcha modullardan qaytish).
"""

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.database.storage import register_participant
from bot.keyboards.inline import age_kb, gender_kb, main_menu_kb, start_kb
from bot.states.user_states import Registration
from bot.texts import messages as msg

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    """/start bosilganda — xush kelibsiz xabari va anonimlik kafolati."""
    await state.clear()  # eski holatlarni tozalaymiz
    await message.answer(msg.WELCOME, reply_markup=start_kb())


@router.callback_query(F.data == "reg:start")
async def on_start_pressed(callback: CallbackQuery, state: FSMContext) -> None:
    """'Boshlash' bosilganda — jins savolini chiqaramiz."""
    await state.set_state(Registration.gender)
    await callback.message.edit_text(msg.ASK_GENDER, reply_markup=gender_kb())
    await callback.answer()


@router.callback_query(Registration.gender, F.data.startswith("reg_gender:"))
async def on_gender_chosen(callback: CallbackQuery, state: FSMContext) -> None:
    """Jins tanlandi — vaqtincha saqlab, yosh savoliga o'tamiz."""
    gender = callback.data.split(":", 1)[1]
    await state.update_data(gender=gender)
    await state.set_state(Registration.age)
    await callback.message.edit_text(msg.ASK_AGE, reply_markup=age_kb())
    await callback.answer()


@router.callback_query(Registration.age, F.data.startswith("reg_age:"))
async def on_age_chosen(callback: CallbackQuery, state: FSMContext) -> None:
    """Yosh tanlandi — ishtirokchini #ID bilan bazaga yozib, bosh menyuni ochamiz."""
    age = callback.data.split(":", 1)[1]
    data = await state.get_data()
    gender = data.get("gender", "—")

    # Anonim #ID beriladi (ism emas, faqat tartib raqami)
    await register_participant(
        telegram_id=callback.from_user.id,
        gender=gender,
        age=age,
    )

    await state.clear()
    await callback.message.edit_text(msg.MAIN_MENU, reply_markup=main_menu_kb())
    await callback.answer()


@router.callback_query(F.data == "menu:main")
async def back_to_main(callback: CallbackQuery, state: FSMContext) -> None:
    """Istalgan moduldan bosh menyuga qaytish."""
    await state.clear()
    await callback.message.edit_text(msg.MAIN_MENU, reply_markup=main_menu_kb())
    await callback.answer()
