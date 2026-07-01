# 📘 Kiber-Himoyachi boti — Kodning to'liq tushuntirishi

> Bu hujjat boshlang'ich dasturchi uchun yozilgan. Biz yozgan har bir faylni
> birma-bir, sodda tilda, misollar bilan tushuntiramiz. Shoshilmang — har bir
> bo'limni o'qib, kodga qarab chiqing.

---

## 1-QISM. Bot umuman qanday ishlaydi?

Telegram bot — bu Telegram serverlari bilan gaplashadigan oddiy dastur.

Tasavvur qiling:
1. Foydalanuvchi botга xabar yozadi (yoki tugma bosadi).
2. Telegram bu xabarni **bizning dasturimizga** yuboradi.
3. Dastur "kim nima yubordi?" ni tekshiradi va mos javobni tayyorlaydi.
4. Javobni yana Telegram orqali foydalanuvchiga qaytaradi.

Bu doimiy takrorlanadigan aylanma jarayon **"polling"** deb ataladi — ya'ni
bizning bot to'xtovsiz Telegram'dan "menga yangi xabar bormi?" deb so'rab turadi.

```
Foydalanuvchi ──► Telegram server ──► BIZNING BOT (dastur)
      ▲                                      │
      └──────────  javob  ◄──────────────────┘
```

Biz bu dasturni **Python** tilida, **aiogram** kutubxonasi yordamida yozdik.
aiogram — Telegram bilan gaplashishning barcha murakkab qismini o'z zimmasiga
oladi, biz esa faqat "qanday javob berish" mantig'ini yozamiz.

---

## 2-QISM. Loyiha xaritasi (papkalar nima uchun?)

```
Kiberxavfsizlik/
├── .env               # MAXFIY: bot tokeni (parol kabi)
├── .gitignore         # GitHub'ga yuklanmasligi kerak bo'lgan fayllar ro'yxati
├── requirements.txt   # Kerakli kutubxonalar ro'yxati
├── README.md          # Loyihani ishga tushirish yo'riqnomasi
└── bot/               # Botning "aqli" — barcha kod shu yerda
    ├── config.py      # Sozlamalarni (token) o'qiydi
    ├── main.py        # Botni ISHGA TUSHIRADI (bosh fayl)
    ├── texts/         # Barcha MATNLAR (xabarlar, savollar)
    ├── keyboards/     # TUGMALAR (menyular)
    ├── states/        # FSM — bot foydalanuvchi "qayerda" ekanini eslaydi
    ├── database/      # Ma'lumotni saqlash (SQLite + Excel)
    └── handlers/      # MANTIQ — "tugma bosilsa nima bo'ladi"
```

**Nega hammasini bitta faylga yozmadik?** Chunki u 1500 qatorli, o'qib
bo'lmaydigan "makaron kod"ga aylanardi. Har bir qismni alohida papkaga
ajratsak: matnni matndan, tugmani tugmadan, mantiqni mantiqdan ajratamiz.
Bu **"vazifalarni ajratish" (separation of concerns)** tamoyili — professional
dasturchilar shunday ishlaydi.


---

## 3-QISM. Kerakli Python tushunchalari (5 daqiqada)

Kodni tushunish uchun 6 ta asosiy tushunchani bilish kifoya:

### 1) `import` — boshqa fayldan narsa olib kelish
```python
from bot.texts import messages as msg
```
"bot/texts/messages.py faylidan hammasini olib kel va uni qisqacha `msg` deb
chaqir". Endi `msg.WELCOME` desak — o'sha fayldagi WELCOME matni chiqadi.

### 2) `def` — funksiya (vazifa)
Funksiya — bu nom berilgan bir bo'lak kod. Chaqirilganda ishlaydi.
```python
def salom():
    print("Salom!")
```

### 3) `async def` va `await` — asinxron funksiya
```python
async def javob(message):
    await message.answer("Salom!")
```
`async` — "bu funksiya boshqalarni kutib turmaydi" degani. Bot bir vaqtda
100 ta odam bilan gaplashishi mumkin, chunki biri javob kutayotganda
ikkinchisiga xizmat qiladi. `await` — "bu amal tugashini kut, lekin boshqa
ishlarni bloklama" degani.

> 🍽 Analogiya: ofitsiant (async) bir stolda ovqat pishishini kutib turmaydi,
> shu vaqtda boshqa stollarga xizmat qiladi. Oddiy (sync) ofitsiant esa bir
> stolda qotib turardi.

### 4) Dekorator — `@router.message(...)`
```python
@router.message(CommandStart())
async def cmd_start(message):
    ...
```
`@` bilan boshlanuvchi qator — bu **dekorator**. U aiogram'ga aytadi:
"agar foydalanuvchi /start yozsa — aynan shu funksiyani ishga tushir".
Ya'ni bu — "qaysi holatda qaysi funksiya ishlaydi" degan ko'rsatma.

### 5) Callback — tugma bosilganda yuboriladigan yashirin signal
Har bir inline tugmaga biz yashirin "belgi" (callback_data) beramiz, masalan
`"menu:a"`. Foydalanuvchi tugmani bosса, Telegram bizga shu belgini yuboradi,
biz esa "aha, demak Test tugmasi bosildi" deb tushunamiz.

### 6) FSM — holat mashinasi (bot xotirasi)
Test paytida bot "bu odam hozir 3-savolda, ballari 7" ni eslab turishi kerak.
FSM (Finite State Machine) aynan shu — foydalanuvchi qaysi bosqichda ekanini
va vaqtinchalik ma'lumotini saqlaydi.


---

## 4-QISM. Fayllarni birma-bir tushuntiramiz

### 📄 4.1. `requirements.txt` — kutubxonalar ro'yxati

```
aiogram==3.13.1        # Telegram bot freymvorki
python-dotenv==1.0.1   # Maxfiy sozlamalarni .env dan o'qish
openpyxl==3.1.5        # Excel (.xlsx) faylga yozish
```

Bu — "xarid ro'yxati". `pip install -r requirements.txt` buyrug'i shu ro'yxatdagi
har bir kutubxonani (aniq versiyasi bilan) o'rnatadi. `==3.13.1` — "aynan shu
versiya" degani. Versiyani qat'iy belgilash muhim: shunda kod bir kompyuterda
ishlab, boshqasida buzilmaydi.

---

### 📄 4.2. `.env` va `.gitignore` — maxfiylik

**`.env`** faylida faqat bitta muhim narsa bor — bot tokeni:
```
BOT_TOKEN=7123456789:AAH-sizning_tokeningiz
```
Token — botingizning **paroli**. Uni kodning ichiga yozib qo'ysak, GitHub'ga
yuklaganda hamma ko'radi va botni o'g'irlaydi. Shuning uchun uni alohida
`.env` fayliga ajratamiz.

**`.gitignore`** — GitHub'ga yuklanmasligi kerak bo'lgan fayllar ro'yxati:
```
.env          # maxfiy token
*.xlsx        # o'quvchilarning ma'lumotlari (maxfiy!)
*.db          # ma'lumotlar bazasi
__pycache__/  # Python'ning vaqtinchalik fayllari
```
Ya'ni bu fayllar sizning kompyuteringizda qoladi, internetга chiqmaydi.

---

### 📄 4.3. `bot/config.py` — sozlamalarni o'qish

Bu fayl `.env` dagi tokenni xavfsiz o'qib oladi.

```python
@dataclass
class Config:
    bot_token: str
    admin_chat_id: int | None = None
    excel_path: Path = BASE_DIR / "malumotlar.xlsx"
```

`@dataclass` — bu ma'lumotlarni chiroyli saqlaydigan "quti" yaratadi. Ichida:
- `bot_token` — token (matn, ya'ni `str`);
- `admin_chat_id` — mutaxassis chati (ixtiyoriy, `None` bo'lishi mumkin);
- `excel_path` — Excel fayl qayerga saqlanishi.

```python
def load_config() -> Config:
    token = os.getenv("BOT_TOKEN")
    if not token or token.startswith("1234567890"):
        raise ValueError("❌ BOT_TOKEN topilmadi...")
    return Config(bot_token=token, admin_chat_id=admin_chat_id)
```

Bu funksiya:
1. `.env` dan tokenni o'qiydi (`os.getenv`);
2. Agar token yo'q bo'lsa yoki namuna qiymat qolgan bo'lsa — **xato beradi**
   (`raise ValueError`). Bu — "himoya to'sig'i": token noto'g'ri bo'lsa, bot
   umuman ishga tushmaydi va sizga aniq sabab aytadi.
3. Hammasi joyida bo'lsa — sozlamalarni `Config` qutisiga solib qaytaradi.


---

### 📄 4.4. `bot/texts/messages.py` — barcha matnlar

Bu faylda botning barcha xabarlari **o'zgaruvchilar (variable)** ko'rinishida
saqlanadi:

```python
WELCOME = (
    "👋 <b>Salom!</b> Raqamli olamdagi xavfsizlik drayveringiz — "
    "<b>Kiber-Himoyachi</b>ga xush kelibsiz!\n\n"
    ...
)
```

Bu yerda:
- `WELCOME` — matnga berilgan nom. Kodning boshqa joyida `msg.WELCOME` desak,
  shu matn chiqadi.
- `<b>...</b>` — bu **HTML teg**, matnni **qalin (bold)** qiladi. (Buni
  ishlashi uchun main.py da `parse_mode=HTML` yoqilgan — pastda ko'ramiz.)
- `\n` — yangi qatorga o'tish belgisi. `\n\n` — bir qator bo'sh joy tashlash.
- Qatorlar qavs `(...)` ichida ketma-ket yozilgan — Python ularni avtomatik
  bitta uzun matnга birlashtiradi.

Ba'zi matnlarда `{score}` kabi "bo'sh joy" bor:
```python
RESULT_MIDDLE = "...Sizning ballingiz: {score} / 27..."
```
Keyinchalik `msg.RESULT_MIDDLE.format(score=21)` desak, `{score}` o'rniga
`21` yoziladi. Bu — matnga o'zgaruvchini "quyish" usuli.

> 💡 **Nega matnlarni alohida faylga chiqardik?** Agar ertaga biror xabarni
> o'zgartirmoqchi bo'lsangiz, kodni titkilamasdan, faqat shu faylni
> tahrirlaysiz. Matn va mantiq aralashmaydi.

---

### 📄 4.5. `bot/texts/questions.py` — test savollari va simulyator

**Test savollari** ro'yxat (list) ko'rinishida saqlangan:

```python
QUESTIONS = [
    {
        "text": "Internetda senga haqoratli sharh yozishsa, nima qilasan?",
        "options": [
            ("Kuchli xavotirga tushaman...", 1),
            ("Jahlim chiqadi...", 2),
            ("Darhol bloklayman...", 3),
        ],
    },
    ... # yana 8 ta savol
]
```

Buni tushunaylik:
- `QUESTIONS` — bu **ro'yxat** (kvadrat qavs `[]`). Ichida 9 ta element bor.
- Har bir element — **lug'at** (dictionary, jingalak qavs `{}`): "kalit: qiymat"
  juftliklari. `"text"` kaliti — savol matni, `"options"` — variantlar.
- Har bir variant — **juftlik**: `("matn", ball)`. Masalan `("Darhol bloklayman", 3)`
  — bu variantni tanласа 3 ball beriladi.

Ballar tizimi: A=1, B=2, C=3. Sog'lom, to'g'ri javob doim eng ko'p ball (3)
oladi. 9 savol × eng ko'pi 3 ball = eng yuqori **27 ball**.

**Simulyator keyslari** ham shunga o'xshash, lekin har variantда "to'g'rimi"
va "izoh" bor:
```python
SIMULATOR = [
    {
        "scenario": "Notanish odam 'yutdingiz, havolaga bosing' deydi...",
        "options": [
            {"text": "Havolaga bosaman", "correct": False, "feedback": "❌ Bu fishing..."},
            {"text": "Bloklayman", "correct": True, "feedback": "✅ Barakalla..."},
        ],
    },
]
```
- `"correct": True/False` — javob to'g'ri yoki noto'g'riligini bildiradi.
- `"feedback"` — o'quvchiga ko'rsatiladigan izoh (nega to'g'ri/xato).


---

### 📄 4.6. `bot/states/user_states.py` — bot xotirasi (FSM)

```python
class Registration(StatesGroup):
    gender = State()
    age = State()

class TestStates(StatesGroup):
    answering = State()

class SupportStates(StatesGroup):
    waiting_message = State()
```

`class` — bu bir-biriga bog'liq narsalarni guruhlaydigan "papka" kabi.
`StatesGroup` — aiogram'ning maxsus "holatlar guruhi".

Bu yerda 3 ta holat guruhi bor:
- **Registration** — ro'yxatdan o'tish: bot `gender` (jins so'ralayotgan) yoki
  `age` (yosh so'ralayotgan) holatida bo'lishi mumkin.
- **TestStates.answering** — foydalanuvchi test yechayotgan holat.
- **SupportStates.waiting_message** — bot foydalanuvchidan anonim xabar
  kutayotgan holat.

**Nega bu kerak?** Masalan, foydalanuvchi anonim xabar yozayotganda, uning
matnini oddiy suhbatdan ajratishimiz kerak. Holat `waiting_message` bo'lsa —
"aha, bu anonim murojaat" deb tushunamiz.

---

### 📄 4.7. `bot/database/storage.py` — ma'lumotni saqlash

Bu eng "texnik" fayl. U ikkita joyga yozadi:
1. **SQLite** (`bot.db`) — ishtirokchilar ro'yxati va ularning #ID raqami.
2. **Excel** (`malumotlar.xlsx`) — SPSS uchun tayyor jadval.

**Nega ikkalasi?** SQLite ID raqamining takrorlanmasligini ishonchli
boshqaradi; Excel esa to'g'ridan-to'g'ri SPSS'ga import qilinadi.

```python
async def register_participant(telegram_id, gender, age) -> int:
    # Bu odam avval qatnashganmi?
    row = conn.execute("SELECT participant_id FROM participants WHERE telegram_id = ?", ...)
    if row is not None:
        return row["participant_id"]   # eski ID'ni qaytaramiz
    # Yangi odam — keyingi raqamni beramiz
    new_id = max_row["m"] + 1
    conn.execute("INSERT INTO participants ...")
    return new_id
```

Bu funksiya foydalanuvchiga **takrorlanmas #ID** beradi. Agar u avval
qatnashgan bo'lsa — eski ID'ni qaytaradi (dublikat bo'lmaydi). Yangi bo'lsa —
oxirgi raqamга +1 qo'shib, yangi ID yaratadi.

> `SELECT`, `INSERT`, `UPDATE` — bu **SQL** buyruqlari (ma'lumot bazasi tili).
> `SELECT` — o'qish, `INSERT` — qo'shish, `UPDATE` — yangilash. `?` belgilari —
> xavfsizlik uchun: qiymatlar o'rniga qo'yiladi (SQL-injection hujumidan himoya).

```python
async def save_result(telegram_id, score, excel_path):
    conn.execute("UPDATE participants SET score = ? ...")   # ballni saqla
    _write_to_excel(excel_path, participant_id, gender, age, score)  # Excelga yoz
```

Test tugagach, bu funksiya ballni bazaga yozadi va Excel qatorini yaratadi:
```
ID       | Jinsi | Yoshi | Ball | Sana
#00001   | Yigit | 14-15 | 21   | 2026-07-01 13:45
```

**Muhim detal — `asyncio.Lock`:**
```python
_lock = asyncio.Lock()
async with _lock:
    ... # yozish amali
```
Bir vaqtda 2 kishi test tugatsa, ular Excelга bir vaqtда yozib, faylni
buzib qo'yishi mumkin. `Lock` (qulf) — "navbat" yaratadi: bir kishi
yozib bo'lmaguncha, ikkinchisi kutadi. Shunda fayl hech qachon buzilmaydi.


---

### 📄 4.8. `bot/keyboards/inline.py` — tugmalar (menyular)

Bu faylda barcha inline tugmalar (xabar ostidagi tugmalar) yasaladi.

```python
def main_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🧪 Kiber-Resilyentlikni tekshirish (Test)", callback_data="menu:a")
    kb.button(text="🚨 Tez yordam: Menga hujum qilishyapti!", callback_data="menu:b")
    kb.button(text="💬 Psixolog bilan anonim chat", callback_data="menu:c")
    kb.adjust(1)
    return kb.as_markup()
```

Buni o'qiylik:
- `InlineKeyboardBuilder()` — tugmalar yig'uvchi "usta".
- `kb.button(text=..., callback_data=...)` — bitta tugma qo'shadi.
  - `text` — tugmada ko'rinadigan yozuv;
  - `callback_data` — tugma bosilganda botga yuboriladigan **yashirin signal**.
    Masalan `"menu:a"` — "Test moduli tanlandi" degani.
- `kb.adjust(1)` — "har bir tugmani alohida qatorga joyla" (1 ta ustun).
- `return kb.as_markup()` — tayyor tugmalar to'plamini qaytaradi.

**Callback signallari qanday tuzilgan?** Biz ularni mantiqiy nomladik:
| Signal | Ma'nosi |
|--------|---------|
| `menu:a` | Test moduliga o'tish |
| `menu:b` | Tez yordam moduliga |
| `menu:c` | Konsultatsiya moduliga |
| `sos:shantaj` | Shantaj SOS zanjiri |
| `sh:money` | Shantaj → "Pul bermaslik" bloki |
| `test_ans:3` | Test javobi = 3 ball |

Ba'zi tugmalar **dinamik** (savolga qarab o'zgaruvchan) yasaladi:
```python
def question_kb(index: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for text, points in QUESTIONS[index]["options"]:
        kb.button(text=text, callback_data=f"test_ans:{points}")
    kb.adjust(1)
    return kb.as_markup()
```
Bu yerda `for` **tsikl** (loop): berilgan savolning 3 ta variantини birma-bir
olib, har biriga tugma yasaydi. `f"test_ans:{points}"` — "f-string": ichidagi
`{points}` o'rniga ball (1, 2 yoki 3) yoziladi. Ya'ni 3-variant tugmasining
signali `test_ans:3` bo'ladi.


---

### 📄 4.9. `bot/handlers/start.py` — boshlang'ich zanjir

Handler — "ushlovchi". Foydalanuvchi biror amal qilса, mos handler uni "ushlab"
javob beradi. Bu fayl /start dan bosh menyugacha bo'lgan yo'lni boshqaradi.

**Router nima?** Har bir handler faylida `router = Router()` bor. Router —
"yo'naltiruvchi": u shu fayldagi barcha handlerlarni bir joyга yig'adi.
Keyin main.py bu routerlarni botga ulaydi.

**1) /start buyrug'i:**
```python
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(msg.WELCOME, reply_markup=start_kb())
```
- `@router.message(CommandStart())` — "agar /start yozilsa, shu funksiyani ishlat".
- `await state.clear()` — eski holatlarni tozalaydi (toza start).
- `await message.answer(...)` — foydalanuvchiга **yangi xabar** yuboradi.
  - `msg.WELCOME` — xush kelibsiz matni;
  - `reply_markup=start_kb()` — xabar ostiga [🚀 Boshlash] tugmasini qo'yadi.

**2) "Boshlash" bosilganda:**
```python
@router.callback_query(F.data == "reg:start")
async def on_start_pressed(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Registration.gender)
    await callback.message.edit_text(msg.ASK_GENDER, reply_markup=gender_kb())
    await callback.answer()
```
- `@router.callback_query(F.data == "reg:start")` — "agar `reg:start` signalli
  tugma bosilsa" (ya'ni Boshlash tugmasi).
- `F.data == "reg:start"` — bu **filtr**: faqat shu signalni ushlaydi. `F` —
  "Magic Filter", ya'ni "kelgan ma'lumotni tekshir" degani.
- `await state.set_state(Registration.gender)` — botni "jins so'ralayotgan"
  holatiга o'tkazadi.
- `callback.message.edit_text(...)` — **eski xabarни o'zgartiradi** (yangi
  yubormaydi!). Shuning uchun savollar ketma-ket "almashib" turadi, chat
  xabarlarga to'lib ketmaydi.
- `await callback.answer()` — tugmadagi aylanuvchi "soat" belgisini o'chiradi
  (Telegram'ga "signalni oldim" deb bildiradi). Buni yozmasak, tugma "osilib"
  qolgandek ko'rinadi.

**3) Jins tanlanganda:**
```python
@router.callback_query(Registration.gender, F.data.startswith("reg_gender:"))
async def on_gender_chosen(callback, state):
    gender = callback.data.split(":", 1)[1]   # "reg_gender:Yigit" -> "Yigit"
    await state.update_data(gender=gender)      # vaqtincha eslab qol
    await state.set_state(Registration.age)     # keyingi bosqich
    await callback.message.edit_text(msg.ASK_AGE, reply_markup=age_kb())
```
- Filtr ikki qismli: `Registration.gender` (faqat shu holatда) VA
  `F.data.startswith("reg_gender:")` (signal shu bilan boshlanса).
- `callback.data.split(":", 1)[1]` — signalni `:` bo'yicha bo'lib, ikkinchi
  qismini oladi. `"reg_gender:Yigit"` → `"Yigit"`.
- `state.update_data(gender=...)` — jinsni FSM xotirasiga vaqtincha yozadi
  (chunki yosh hali tanlanmagan, ID keyin beriladi).

**4) Yosh tanlanganda — ro'yxatga olish:**
```python
@router.callback_query(Registration.age, F.data.startswith("reg_age:"))
async def on_age_chosen(callback, state):
    age = callback.data.split(":", 1)[1]
    data = await state.get_data()          # oldin saqlangan jinsni olamiz
    gender = data.get("gender", "—")
    await register_participant(callback.from_user.id, gender, age)  # #ID beriladi
    await state.clear()
    await callback.message.edit_text(msg.MAIN_MENU, reply_markup=main_menu_kb())
```
Bu yerda jins va yosh birlashadi, `register_participant` chaqirilib,
foydalanuvchiga anonim #ID beriladi va bazага yoziladi. So'ng bosh menyu ochiladi.

**5) Bosh menyuga qaytish:**
```python
@router.callback_query(F.data == "menu:main")
async def back_to_main(callback, state):
    await state.clear()
    await callback.message.edit_text(msg.MAIN_MENU, reply_markup=main_menu_kb())
```
Istalgan moduldan "🏠 Bosh menyu" bosilса, shu handler ishlaydi.


---

### 📄 4.10. `bot/handlers/module_a.py` — diagnostika testi

Bu — testning "aqli". U savollarni ketma-ket ko'rsatadi, ballni yashirin
hisoblaydi va natijани chiqaradi.

**1) Testni boshlash:**
```python
@router.callback_query(F.data == "menu:a")
async def start_test(callback, state):
    await state.set_state(TestStates.answering)
    await state.update_data(index=0, score=0)   # savol raqami=0, ball=0
    await _show_question(callback, index=0)
```
Test boshlanganda 2 ta hisoblagichni nolga qo'yamiz:
- `index=0` — hozirgi savol raqami (0 dan boshlanadi, ya'ni 1-savol);
- `score=0` — to'plangan ball.
Bular FSM xotirasiga yoziladi va butun test davomida yangilanib boradi.

**2) Savolni ko'rsatish (yordamchi funksiya):**
```python
async def _show_question(callback, index):
    question = QUESTIONS[index]
    text = f"🧪 Savol {index + 1}/{len(QUESTIONS)}\n\n{question['text']}"
    await callback.message.edit_text(text, reply_markup=question_kb(index))
```
- `QUESTIONS[index]` — ro'yxatdan `index`-savolni oladi.
- `f"...Savol {index + 1}/{len(QUESTIONS)}..."` — "Savol 1/9" kabi sarlavha
  yasaydi. (`index+1` chunki kompyuter 0 dan sanaydi, odam 1 dan.)
- `question_kb(index)` — o'sha savolning 3 ta variant tugmasini yasaydi.

**3) Javob bosilganda — eng muhim qism:**
```python
@router.callback_query(TestStates.answering, F.data.startswith("test_ans:"))
async def on_answer(callback, state):
    points = int(callback.data.split(":", 1)[1])   # "test_ans:3" -> 3
    data = await state.get_data()
    index = data["index"] + 1        # keyingi savolga o'tamiz
    score = data["score"] + points   # ballni qo'shamiz

    if index < len(QUESTIONS):
        # Yana savol bor
        await state.update_data(index=index, score=score)
        await _show_question(callback, index=index)
    else:
        # Test tugadi!
        await state.clear()
        await save_result(callback.from_user.id, score, _config.excel_path)
        await _show_result(callback, score)
```
Bu funksiya har javobda ishlaydi:
1. Bosilgan tugmadan ballни oladi (`int(...)` — matnni songa aylantiradi).
2. Savol raqamini +1 qiladi, ballni qo'shadi.
3. **Agar yana savol bo'lsa** (`index < 9`) — keyingi savolни ko'rsatadi.
4. **Agar oxirgi savol bo'lса** — testni tugatadi: ballni bazaga yozadi va
   natijани chiqaradi.

Ana shu `if/else` — testning yuragi. Foydalanuvchi buни ko'rmaydi, lekin
orqa fonda ball to'planib boradi.

**4) Natijани ko'rsatish:**
```python
async def _show_result(callback, score):
    if score <= 15:
        text, level = msg.RESULT_HIGH_RISK, "risk"
    elif score <= 22:
        text, level = msg.RESULT_MIDDLE, "middle"
    else:
        text, level = msg.RESULT_HIGH_IMMUNITY, "high"
    await callback.message.edit_text(text.format(score=score), reply_markup=result_kb(level))
```
Ballga qarab 3 xil natijadan birини tanlaydi:
- **9–15 ball** → Yuqori xavf guruhi;
- **16–22 ball** → O'rta (barqaror);
- **23–27 ball** → Yuqori kiber-immunitet.
`text.format(score=score)` — matndagi `{score}` o'rniga haqiqiy ballni qo'yadi.


---

### 📄 4.11. `bot/handlers/module_b.py` — Tez yordam (SOS) va Simulyator

Bu eng katta handler, lekin mantig'i sodda: har bir tugma bir blokni ochadi.

**Yordamchi funksiya `_edit` — kod takrorlanmasligi uchun:**
```python
DELAY_SECONDS = 1.5

async def _edit(callback, text, keyboard, delay=False):
    if delay:
        await callback.answer()
        await asyncio.sleep(DELAY_SECONDS)   # 1.5 soniya kutish
    await callback.message.edit_text(text, reply_markup=keyboard)
    if not delay:
        await callback.answer()
```
Har bir blokда "xabarni o'zgartir + tugmani javob ber" takrorlanadi. Buni
har safar yozmaslik uchun bitta yordamchiга yig'dik. `delay=True` bo'lsa,
avval **1.5 soniya kutadi** — foydalanuvchi tashvishli matnни o'qib ulgursin
va hamma tugmani birdan bosib yubormasin (topshiriqdagi talab).

> `asyncio.sleep(1.5)` — "1.5 soniya kut, lekin boshqa foydalanuvchilarни
> bloklama". Oddiy `time.sleep` bo'lganda butun bot muzlab qolardi.

**SOS zanjiri — har blok bir handler:**
```python
@router.callback_query(F.data == "sos:shantaj")
async def sh_start(callback):
    await _edit(callback, msg.SH_START, sh_start_kb(), delay=True)

@router.callback_query(F.data == "sh:money")
async def sh_money(callback):
    await _edit(callback, msg.SH_NO_MONEY, sh_money_kb())
```
Ko'ryapsizmi? Har bir tugma → o'z handleri → o'z matni + keyingi tugmalar.
Bu **"zanjir"**: `sos:shantaj` → `sh:money` → `sh:evidence` → `sh:block` →
`sh:legal`. Foydalanuvchi tugmalarni bosib, blokdan blokga o'tadi.

Xuddi shu tarzda:
- **Bulling zanjiri:** `sos:bulling` → `bl:noresp` → `bl:facts` → `bl:shield` → `bl:legal`;
- **Akkaunt/fishing zanjiri:** `sos:akkaunt` → `ak:pass` → `ak:2fa` → `ak:report` → `ak:legal`.

**Simulyator — biroz murakkabroq (raqamli signallar):**
```python
@router.callback_query(F.data.startswith("simans:"))
async def sim_answer(callback):
    _, case_str, option_str = callback.data.split(":")   # "simans:0:1"
    case_index = int(case_str)      # qaysi keys
    option_index = int(option_str)  # qaysi variant
    option = SIMULATOR[case_index]["options"][option_index]
    await callback.message.edit_text(option["feedback"], reply_markup=sim_next_kb(case_index + 1))
    await callback.answer("To'g'ri! 🎉" if option["correct"] else "Keling, tahlil qilamiz 🤔")
```
Bu yerdagi signal 3 qismli: `simans:0:1` = "simulyator javobi, 0-keys, 1-variant".
- `callback.data.split(":")` — uni 3 bo'lakka ajratadi;
- keys va variant raqamlari bo'yicha to'g'ri izohni (`feedback`) topamiz;
- `callback.answer(... if ... else ...)` — bu **shartli ifoda**: javob to'g'ri
  bo'lsa "To'g'ri! 🎉", xato bo'lsa "Keling, tahlil qilamiz 🤔" chiqadi
  (ekran tepasida qisqa bildirishnoma).


---

### 📄 4.12. `bot/handlers/module_c.py` — konsultatsiya va anonim aloqa

**1) Konsultatsiya matnini tanlash — "lug'at" hiylasi:**
```python
_CONSULT_TEXTS = {
    "shantaj": msg.C_SHANTAJ,
    "bulling": msg.C_BULLING,
    "fraud":   msg.C_FRAUD,
}

@router.callback_query(F.data.startswith("c:"))
async def show_consultation(callback):
    topic = callback.data.split(":", 1)[1]   # "c:shantaj" -> "shantaj"
    text = _CONSULT_TEXTS.get(topic)
    await callback.message.edit_text(text, reply_markup=consult_kb())
```
Bu chiroyli usul: 3 ta tugma uchun 3 ta alohida handler yozish o'rniga,
**bitta** handler yozdik. `_CONSULT_TEXTS` lug'ati "mavzu → matn" bog'lanишини
saqlaydi. Foydalanuvchi qaysi mavzuni tanlasa, `.get(topic)` o'sha matnni
topib beradi. Kod qisqa va toza.

**2) Anonim aloqani boshlash — maxfiy raqam:**
```python
@router.callback_query(F.data == "cchat:start")
async def start_anon_chat(callback, state):
    code = f"M-{secrets.randbelow(90000) + 10000}"   # masalan M-48213
    await state.set_state(SupportStates.waiting_message)
    await state.update_data(secret_code=code)
    await callback.message.edit_text(msg.C_ANON_CHAT_START.format(code=code))
```
- `secrets.randbelow(90000) + 10000` — 10000..99999 oralig'ida **tasodifiy son**
  yaratadi (5 xonali maxfiy raqam). `secrets` — xavfsiz tasodif kutubxonasi.
- Botni `waiting_message` holatiga o'tkazamiz — endi keyingi yozilgan xabar
  "anonim murojaat" deb qabul qilinadi.

**3) Anonim xabarni qabul qilish:**
```python
@router.message(SupportStates.waiting_message)
async def receive_anon_message(message, state):
    data = await state.get_data()
    code = data.get("secret_code", "M-00000")
    await state.clear()
    if _config.admin_chat_id is not None:
        await message.copy_to(chat_id=_config.admin_chat_id)   # mutaxassisga uzat
    await message.answer(msg.C_ANON_CHAT_SAVED.format(code=code), reply_markup=back_to_menu_kb())
```
- `@router.message(SupportStates.waiting_message)` — "faqat shu holatda kelgan
  xabarni ushla" (oddiy /start dan farqli).
- `message.copy_to(...)` — xabarни mutaxassis chatiga **nusxalab** yuboradi.
  ⚠️ Muhim: `copy_to` — `forward` (yo'naltirish) emas! Forward qilганда
  yuboruvchining ismi ko'rinardi. `copy_to` esa faqat matnni uzatadi, kim
  yozgani **ko'rinmaydi** — anonimlik saqlanadi.
- Agar mutaxassis chati sozlanmagan bo'lsa (`admin_chat_id is None`), xabar
  shunchaki qabul qilinadi (keyinroq sozlash mumkin).


---

### 📄 4.13. `bot/main.py` — botni ishga tushiruvchi bosh fayl

Bu — botning "start tugmasi". Barcha qismlarni birlashtirib, ishga tushiradi.

```python
async def main():
    config = load_config()
    bot = Bot(token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(module_a.router)
    dp.include_router(module_b.router)
    dp.include_router(module_c.router)

    await init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
```

Qadam-qadam:
1. `config = load_config()` — `.env` dan tokenни o'qiydi.
2. `bot = Bot(...)` — Telegram bilan gaplashuvchi "bot" obyektini yaratadi.
   - `parse_mode=ParseMode.HTML` — matnlardagi `<b>...</b>` teglari ishlashini
     yoqadi (qalin matn). Buni yoqmasак, foydalanuvchi `<b>` belgилarini
     ko'rib qolardi.
3. `dp = Dispatcher()` — **dispetcher**: kelgan xabarni to'g'ri handlerga
   yo'naltiruvchi "markaziy telefon stansiyasi".
4. `dp.include_router(...)` — 4 ta modul routerини botga ulaydi. Endi
   dispetcher barcha handlerlarni "biladi".
5. `await init_db()` — ma'lumotlar bazasini tayyorlaydi (jadval yaratadi).
6. `await bot.delete_webhook(drop_pending_updates=True)` — bot o'chiq turган
   paytdagi eski xabarlarни tashlab yuboradi (toza start).
7. `await dp.start_polling(bot)` — **polling**ни boshlaydi: bot endi
   to'xtovsiz Telegram'dan "yangi xabar bormi?" deb so'rab turadi.

```python
if __name__ == "__main__":
    asyncio.run(main())
```
Bu qator — "agar bu fayl to'g'ridan-to'g'ri ishga tushirilsa
(`python -m bot.main`), `main()` funksiyasini boshla" degani.
`asyncio.run(...)` — asinxron dunyoni ishga soluvchi "kalit".

---

## 5-QISM. Umumiy oqim (hamma narsa qanday bog'lanadi?)

Foydalanuvchi /start bosgandan test natijasigacha bo'lgan yo'l:

```
1. Foydalanuvchi: /start
   └─► main.py polling ushlaydi ─► start.py: cmd_start()
        └─► msg.WELCOME + start_kb() [🚀 Boshlash]

2. [🚀 Boshlash] bosildi (signal: reg:start)
   └─► start.py: on_start_pressed() ─► holat: Registration.gender
        └─► msg.ASK_GENDER + gender_kb() [Yigit][Qiz]

3. [Yigit] bosildi (signal: reg_gender:Yigit)
   └─► start.py: on_gender_chosen() ─► jinsni FSM ga saqlaydi ─► holat: age
        └─► msg.ASK_AGE + age_kb()

4. [14-15] bosildi (signal: reg_age:14-15)
   └─► start.py: on_age_chosen()
        └─► storage.py: register_participant() ─► #ID beriladi, bazaga yoziladi
        └─► msg.MAIN_MENU + main_menu_kb()

5. [🧪 Test] bosildi (signal: menu:a)
   └─► module_a.py: start_test() ─► holat: TestStates.answering
        └─► 1-savol ... 9-savolgacha (on_answer har javobda ball qo'shadi)
             └─► oxirgi javob ─► storage.py: save_result() ─► Excelga yoziladi
                  └─► msg natija (ballga qarab) + result_kb()
```

Ana shu — butun tizim. Har bir tugma bir signal yuboradi, signal mos handlerни
uyg'otadi, handler matnни o'zgartirib, keyingi tugmalarни chiqaradi. Oddiy,
lekin kuchli!

---

## 6-QISM. Kichik lug'at (glossary)

| Atama | Oddiy tushuntirish |
|-------|--------------------|
| **Bot** | Telegram bilan gaplashadigan dastur |
| **aiogram** | Bot yozishni osonlashtiradigan Python kutubxonasi |
| **Token** | Botning maxfiy paroli (BotFather beradi) |
| **Handler** | "Ushlovchi" — biror amalga javob beruvchi funksiya |
| **Router** | Handlerlarни guruhlab, botga ulovchi |
| **Dispatcher** | Kelgan xabarни to'g'ri handlerга yo'naltiruvchi |
| **Callback** | Tugma bosilganda yuboriladigan yashirin signal |
| **Inline tugma** | Xabar ostidagi bosiladigan tugma |
| **FSM / State** | Bot xotirasi — foydalanuvchi "qayerda" ekanini eslaydi |
| **async / await** | Bir vaqtda ko'p odam bilan ishlash imkoni |
| **Dekorator (@)** | "Bu funksiya qachon ishlaydi" degan ko'rsatma |
| **polling** | Botning "yangi xabar bormi?" deb so'rab turishi |
| **SQLite** | Kichik ma'lumotlar bazasi (fayl ichida) |
| **openpyxl** | Excel fayl bilan ishlash kutubxonasi |

---

## 🎓 Yakuniy so'z

Tabriklayman! Endi siz nafaqat ishlaydigan botга egasiz, balki uning **har bir
qatorini tushunasiz**. Bu — haqiqiy dasturchiga xos xususiyat: kodni ko'chirib
emas, **tushunib** ishlatish.

Maslahat: bu hujjatни ochib qo'yib, `bot/` papkasidagi haqiqiy fayllarни yonma-yon
o'qing. Har bir tushuntirishni kodda toping. Shunda bilim mustahkamlanadi. 💪
