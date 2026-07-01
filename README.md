# 🛡 Kiber-Himoyachi — Telegram bot

O'smirlarni internetdagi kiber hujumlardan (shantaj, kiberbulling, firibgarlik)
himoya qiluvchi bot. Bot **psixologik yordam** va **yuridik maslahat** beradi,
hamda ilmiy tahlil (SPSS) uchun anonim ma'lumot yig'adi.

Texnologiya: **Python + aiogram 3.x**, ma'lumot **SQLite + Excel** ga yoziladi.

---

## 📂 Loyiha tuzilishi

```
bot/
├── config.py          # Token va sozlamalar (.env dan o'qiladi)
├── main.py            # Ishga tushirish nuqtasi (routerlarni ulaydi)
├── handlers/          # Mantiq
│   ├── start.py       # /start zanjiri, sotsiologik pasport, bosh menyu
│   ├── module_a.py    # Diagnostika testi (9 savol, ball, natija)
│   ├── module_b.py    # SOS (Shantaj/Bulling/Akkaunt) + Kiber-Simulyator
│   └── module_c.py    # Konsultatsiya + anonim mutaxassisga eskalatsiya
├── keyboards/inline.py # Barcha inline tugmalar
├── texts/             # Barcha matnlar va savollar
├── states/            # FSM holatlari
└── database/storage.py # SQLite + Excel (SPSS uchun)
```

---

## 🚀 Ishga tushirish (o'z kompyuteringizda)

### 1. Python o'rnatilganini tekshiring (3.10+)
```bash
python --version
```

### 2. Loyihani yuklab oling
```bash
git clone https://github.com/dkurbanov2003-star/Kiberxavfsizlik.git
cd Kiberxavfsizlik
```

### 3. Virtual muhit yarating va kutubxonalarni o'rnating
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 4. Tokenni sozlang
`.env.example` faylidan nusxa olib `.env` yarating va tokeningizni qo'ying:
```bash
# Windows: copy .env.example .env
cp .env.example .env
```
`.env` ichida:
```
BOT_TOKEN=BotFatherdan_olgan_tokeningiz
ADMIN_CHAT_ID=      # ixtiyoriy (anonim murojaatlar uchun)
```

### 5. Botni ishga tushiring
```bash
python -m bot.main
```
Terminalda `Bot ishga tushmoqda...` chiqsa — Telegram'da botingizga `/start` yozing! 🎉

---

## 📊 Ma'lumotlar (SPSS uchun)

Har bir yakunlangan test `malumotlar.xlsx` fayliga bitta qator qilib yoziladi:

| ID | Jinsi | Yoshi | Ball | Sana |
|----|-------|-------|------|------|
| #00001 | Yigit | 14-15 | 21 | 2026-07-01 14:30 |

Bu faylni to'g'ridan-to'g'ri SPSS yoki Excel'da ochib tahlil qilish mumkin.

**Ball shkalasi (9 savol × 1–3 ball = 9–27):**
- **9–15** — Yuqori xavf guruhi
- **16–22** — O'rta (barqaror) guruh
- **23–27** — Yuqori kiber-immunitet

---

## 🔐 Xavfsizlik

- `.env`, `*.xlsx`, `*.db` fayllari `.gitignore` orqali GitHub'ga **yuklanmaydi**.
- Bot foydalanuvchi ismi/telefonini saqlamaydi — faqat anonim `#ID`, jins, yosh, ball.
```
