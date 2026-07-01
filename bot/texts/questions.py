"""
questions.py — Modul A test savollari va Modul B simulyator keyslari.

TEST SAVOLLARI:
  Har bir savolda 3 ta variant bor. Ballari: A=1, B=2, C=3.
  Har bir variant (matn, ball) juftligi sifatida saqlanadi.
  Jami 9 savol => eng kam 9, eng ko'p 27 ball.
"""

# I, II, III bloklar ketma-ket birlashtirilgan (foydalanuvchi uchun uzluksiz oqim)
QUESTIONS: list[dict] = [
    # --- I-BLOK: Kiber-resilyentlik ---
    {
        "text": "Internetda senga nisbatan haqoratli sharh yozishsa, birinchi bo'lib nima qilasan?",
        "options": [
            ("Kuchli xavotirga tushaman, uzoq o'ylab yuraman", 1),
            ("Jahlim chiqadi, undan alamliroq javob qaytaraman", 2),
            ("Darhol bloklayman yoki e'tibor bermayman", 3),
        ],
    },
    {
        "text": "Onlayn o'yin yoki ijtimoiy tarmoqda muvaffaqiyatsizlikka uchrasang "
                "(akkaunt o'chsa/bloklansa), o'zingni qanday his qilasan?",
        "options": [
            ("Dunyo ko'zimga qorong'u bo'ladi, hamma ishdan ko'nglim soviydi", 1),
            ("Asabiylashaman, lekin tezda yangi akkaunt ochaman", 2),
            ("Bu virtual olam ekanini tushunaman, xotirjam qabul qilaman", 3),
        ],
    },
    {
        "text": "Kimdir bosim o'tkazsa yoki ustingdan kulsa, bu holatdan chiqishga qancha vaqt ketadi?",
        "options": [
            ("Bir necha kun tushkunlikda yuraman", 1),
            ("O'sha kuni asabiylashaman, ertasiga esdan chiqadi", 2),
            ("Bir necha daqiqada chalg'iy olaman", 3),
        ],
    },
    # --- II-BLOK: Kiber-viktimizatsiya xavfi ---
    {
        "text": "Do'stingdan \"Tanlovda menga ovoz ber, mana havola\" degan xabar kelsa, nima qilasan?",
        "options": [
            ("Darhol ssilkaga bosaman va kodlarni kiritaman", 1),
            ("Shubhalanaman, lekin baribir bosib ko'raman", 2),
            ("Bosmayman, do'stimga boshqa kanal orqali bog'lanib tekshiraman", 3),
        ],
    },
    {
        "text": "Yangi tanishing \"Bu gaplar sir qolsin, hech kimga aytma\" desa, munosabating qanday?",
        "options": [
            ("Ishonganidan xursand bo'laman, sirni saqlayman", 1),
            ("G'alati tuyuladi, lekin muloqotni davom ettiraman", 2),
            ("Shubhalanaman, muloqotni cheklayman, yaqinlarimga aytaman", 3),
        ],
    },
    {
        "text": "Internetdagi tanishing \"Parolingni ber, senga qimmatbaho skin/akkaunt sovg'a "
                "qilaman\" desa, nima qilasan?",
        "options": [
            ("Ishonib parolimni beraman", 1),
            ("Avval u va'dasini bajarsa, keyin o'ylayman", 2),
            ("Hech qachon parolimni bermayman, buni firibgarlik deb bilaman", 3),
        ],
    },
    # --- III-BLOK: Ijtimoiy-oilaviy omil ---
    {
        "text": "Kimdir shaxsiy rasming/sirlaring bilan shantaj qilsa, birinchi bo'lib kimga murojaat qilasan?",
        "options": [
            ("Hech kimga aytolmayman, ota-onam jazolashidan qo'rqaman", 1),
            ("Faqat tengdosh do'stlarimga aytaman", 2),
            ("Darhol ota-onamga yoki ishongan kattaga aytaman", 3),
        ],
    },
    {
        "text": "Ota-onang internetdagi hayotingga qanchalik qiziqadi?",
        "options": [
            ("Qiziqishmaydi yoki faqat telefonni olib qo'yish bilan tahdid qilishadi", 1),
            ("Ba'zida yuzaki so'rab turishadi", 2),
            ("Doimiy qiziqishadi, jazolamasdan do'stona maslahat berishadi", 3),
        ],
    },
    {
        "text": "Jiddiy xato qilsang (masalan noto'g'ri rasm yuborsang), oilang qanday munosabatda bo'ladi?",
        "options": [
            ("Qattiq jazolashadi, telefonsiz qoldirishadi", 1),
            ("Urishishadi, lekin muammoni hal qilib berishadi", 2),
            ("Tushunishadi, kechirishadi, birgalikda yechim qidirishadi", 3),
        ],
    },
]


# ============================================================
#  MODUL B — KIBER-SIMULYATOR KEYSLARI
#  Eslatma: bu 3 keys topshiriq ruhida namuna sifatida yozildi.
#  To'g'ri javob "correct": True. Xato tanlansa — psixologik tuzoq tushuntiriladi.
# ============================================================

SIMULATOR: list[dict] = [
    {
        "scenario": (
            "🎮 <b>1-KEYS.</b> Notanish odam sizga yozadi: \"Sizning akkauntingiz "
            "tanlovda yutdi! 🎁 Sovg'ani olish uchun quyidagi havolaga kirib, "
            "Telegram kodingizni kiriting\". Nima qilasiz?"
        ),
        "options": [
            {"text": "Havolaga kirib kodni kiritaman", "correct": False,
             "feedback": "❌ Bu — fishing tuzog'i! Telegram kodini kiritsangiz, "
                         "akkauntingiz o'g'irlanadi. Hech kim, hatto tanlovlar ham "
                         "sizning kirish kodingizni so'ramaydi."},
            {"text": "Havolani tekshirmasdan o'chirib, bloklayaman", "correct": True,
             "feedback": "✅ Barakalla! Kutilmagan \"yutuq\" xabarlari deyarli doim "
                         "firibgarlikdir. Kodni hech kimga bermaslik — eng to'g'ri qaror."},
            {"text": "Do'stlarimga yuboraman, ular ham yutsin", "correct": False,
             "feedback": "❌ Bu tuzoqni tarqatib, do'stlaringizni ham xavf ostiga "
                         "qo'yasiz. Shubhali havolalarni hech kimga ulashmang."},
        ],
    },
    {
        "scenario": (
            "🎮 <b>2-KEYS.</b> Onlayn tanishingiz siz bilan bir necha kun "
            "chiroyli suhbatlashdi. Endi u: \"Menga ishonasanmi? Bitta shaxsiy "
            "rasmingni yubor, bu bizning sirimiz bo'ladi\" deydi. Nima qilasiz?"
        ),
        "options": [
            {"text": "Ishonaman, rasmni yuboraman", "correct": False,
             "feedback": "❌ \"Bu bizning sirimiz\" iborasi — grooming (bola bilan "
                         "manipulyatsiya) belgisidir. Bunday rasm keyinchalik "
                         "shantaj quroliga aylanishi mumkin."},
            {"text": "Rad etaman va yaqin kattamga aytaman", "correct": True,
             "feedback": "✅ To'g'ri! Sirni saqlashni talab qilish — xavf signali. "
                         "Kattaga aytish sizni himoya qiladi, bu chaqimchilik emas."},
            {"text": "Yubormaymanu, lekin suhbatni davom ettiraman", "correct": False,
             "feedback": "⚠️ Rasm yubormaganingiz yaxshi, lekin bunday odam bilan "
                         "muloqotni davom ettirish xavfli. Aloqani cheklang va kattaga ayting."},
        ],
    },
    {
        "scenario": (
            "🎮 <b>3-KEYS.</b> Sinfdoshlaringiz guruhda siz haqingizda "
            "masxaralovchi rasm (mem) tarqatib, ustingizdan kulishmoqda. "
            "Nima qilasiz?"
        ),
        "options": [
            {"text": "Men ham ularni haqorat qilib javob yozaman", "correct": False,
             "feedback": "❌ Javob yozsangiz, ularga \"ozuqa\" berasiz va janjal "
                         "kuchayadi. Bu aynan ular kutayotgan reaksiya."},
            {"text": "Skrinshot qilib, keyin bloklab, kattaga (o'qituvchi/ota-ona) aytaman", "correct": True,
             "feedback": "✅ A'lo! Avval dalil (skrinshot), keyin ignor va katta "
                         "yordami — kiberbullingni to'xtatishning eng samarali yo'li."},
            {"text": "Guruhdan jimgina chiqib, hech kimga aytmayman", "correct": False,
             "feedback": "⚠️ Chiqib ketish yordam berishi mumkin, lekin dalilsiz va "
                         "kattaning yordamisiz bezorilar boshqalarga o'tadi. Albatta xabar bering."},
        ],
    },
]
