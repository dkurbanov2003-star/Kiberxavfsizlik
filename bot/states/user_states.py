"""
user_states.py — FSM (holat mashinasi) holatlari.

FSM bot foydalanuvchi qaysi bosqichda turganini "eslab qolishi" uchun kerak.
Masalan: test paytida qaysi savolda ekani yoki anonim xabar kutilayotgani.
"""

from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    """Sotsiologik pasport bosqichi (jins -> yosh)."""
    gender = State()
    age = State()


class TestStates(StatesGroup):
    """Modul A — diagnostika testi davom etayotgan holat."""
    answering = State()


class SupportStates(StatesGroup):
    """Modul C — anonim xabar kutilayotgan holat."""
    waiting_message = State()
