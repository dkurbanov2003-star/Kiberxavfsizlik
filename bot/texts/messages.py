"""
messages.py — Botning barcha statik matnlari.

Matnlarni kod mantiqidan ajratib saqlaymiz. Shunda:
  - matnni tahrirlash oson (kodni buzmasdan);
  - kod toza va o'qilishi qulay bo'ladi.
Bold uchun HTML teglari (<b>...</b>) ishlatilgan (parse_mode=HTML).
"""

# ============================================================
#  MODUL /start — BOSHLANG'ICH ZANJIR
# ============================================================

WELCOME = (
    "👋 <b>Salom!</b> Raqamli olamdagi xavfsizlik drayveringiz — "
    "<b>Kiber-Himoyachi</b>ga xush kelibsiz!\n\n"
    "Bu yerda siz internetdagi har qanday vaziyat (haqorat, shantaj yoki "
    "firibgarlik) bo'yicha <b>mutlaqo anonim</b> yordam olishingiz mumkin.\n\n"
    "🔒 Ismingiz, telefoningiz yoki profilingiz hech kimga ko'rinmaydi va "
    "ota-onangiz yoki maktabingizga yuborilmaydi. Bu yerda hamma narsa sir qoladi!"
)

ASK_GENDER = "📊 Statistika to'g'ri hisoblanishi uchun jinsingizni belgilang:"

ASK_AGE = "🎂 Yoshingizni tanlang:"

MAIN_MENU = "✨ <b>Ajoyib!</b> Endi o'zingizga kerakli bo'limni tanlang:"


# ============================================================
#  MODUL A — DIAGNOSTIKA (TEST) NATIJALARI
# ============================================================
# Eslatma: test 9 ta savoldan iborat, har biri 1–3 ball => jami 9–27 ball.
# Interpretatsiya (topshiriqdagi "Umumiy ballar" bo'yicha):
#   9–15  -> Yuqori xavf guruhi
#   16–22 -> O'rta (barqaror) guruh
#   23–27 -> Yuqori kiber-immunitet

RESULT_HIGH_IMMUNITY = (
    "🏅 <b>Barakalla! Siz raqamli olamda haqiqiy Kiber-Skaut ekansiz!</b>\n\n"
    "Internetdagi xavflarni juda yaxshi farqlay olasiz, manipulyatsiyalarga "
    "uchmaysiz va emotsiyalaringizni nazorat qila olasiz. Ushbu bilimingiz "
    "sizni kiberhujumlardan ishonchli himoya qiladi.\n\n"
    "Agar do'stlaringiz kiberxavfga duch kelishsa, ularga ham ushbu botni tavsiya qiling!\n\n"
    "📈 <b>Sizning ballingiz: {score} / 27</b> — Yuqori kiber-immunitet."
)

RESULT_MIDDLE = (
    "👍 <b>Yaxshi natija!</b>\n\n"
    "Siz internet qoidalarini bilasiz, lekin ba'zida kiberjinoyatchilarning "
    "ayyorona tuzoqlariga (shantaj yoki fishing) chalg'ib qolishingiz xavfi bor.\n\n"
    "Raqamli immunitetingizni yanada kuchaytirish uchun quyidagi tugmani bosing:\n\n"
    "📈 <b>Sizning ballingiz: {score} / 27</b> — O'rta (barqaror) guruh."
)

RESULT_HIGH_RISK = (
    "🛡 <b>Siz testdan o'tdingiz.</b>\n\n"
    "Hozirgi kunda internet olami juda ko'p ayyorona tuzoqlardan iborat bo'lib, "
    "ularga aldanib qolish hech gap emas. <b>Bu sizning aybingiz emas.</b>\n\n"
    "Raqamli xavfsizligingizni oshirish uchun biz sizga maxsus yo'riqnomalarni "
    "tayyorladik. Zudlik bilan tanishing:\n\n"
    "📈 <b>Sizning ballingiz: {score} / 27</b> — Yuqori xavf guruhi."
)


# ============================================================
#  MODUL B — SOS (SHANTAJ) ZANJIRI
# ============================================================

SOS_MENU = (
    "🚨 <b>Tez yordam</b>\n\n"
    "Chuqur nafas oling. Sizga qanday hujum bo'layotganini tanlang — "
    "men sizga qadamma-qadam yordam beraman:"
)

SIM_OR_SOS = (
    "🧭 <b>Modul B — Himoya markazi</b>\n\n"
    "Ikki rejim mavjud. Qaysi biri sizga kerak?\n\n"
    "• <b>SOS</b> — hoziroq hujumga uchrayapsiz;\n"
    "• <b>Kiber-Simulyator</b> — xavflarni oldindan mashq qilib o'rganish."
)

# --- Shantaj bloklari ---
SH_START = (
    "🛑 <b>To'xtang! Chuqur nafas oling.</b>\n\n"
    "Hozir ichingizdan o'tayotgan qo'rquv, xavotir va sharmandalik hissi "
    "butunlay normal holat. Lekin bir narsani unutmang: "
    "<b>Siz aybdor emassiz, siz qurbonsiz!</b>\n\n"
    "Jinoyatchining yagona quroli — sizning qo'rquvingiz. Biz hozir buni "
    "birgalikda to'xtatamiz. Quyidagi 3 qoidadan boshlang (har birini tartib bilan bosing):"
)

SH_NO_MONEY = (
    "💸 <b>1-QOIDA: JINOYATCHIGA PUL BERMANG!</b>\n\n"
    "Shantajchilar pul olgach, sizni hech qachon tinch qo'yishmaydi, aksincha "
    "yanada ko'proq talab qilishadi. Pul to'lash — muammoning yechimi emas, "
    "balki tuzoqning chuqurlashishidir. <b>Pul bermang!</b>"
)

SH_EVIDENCE = (
    "📸 <b>2-QOIDA: DALILLARNI SAQLAB QOLING!</b>\n\n"
    "Yozishmalarni o'chirmang. Barcha tahdidlar, pul so'ralgan xabarlar va "
    "jinoyatchining profil havolasini (link yoki ID) zudlik bilan skrinshot qiling. "
    "Bu skrinshotlar kelgusida sizni huquqiy himoya qilish uchun yagona rasmiy dalil bo'ladi."
)

SH_BLOCK = (
    "🚫 <b>3-QOIDA: ALOQANI MUTLAQO UZING!</b>\n\n"
    "Jinoyatchi bilan tortishmang, o'zingizni oqlashga urinmang. Dalillarni "
    "saqlab bo'lgach, uni barcha ijtimoiy tarmoqlarda bloklang. Emotsional "
    "aloqani uzganingizdan keyin jinoyatchining ta'sir kuchi 80% ga pasayadi."
)

SH_LEGAL = (
    "⚖️ <b>SIZNING HUQUQLARINGIZ:</b>\n\n"
    "1) <b>Qonun siz tomonda.</b> O'zbekiston Respublikasi Jinoyat kodeksining "
    "165-moddasiga ko'ra, shantaj (tovlamachilik) og'ir jinoyat hisoblanadi. "
    "Skrinshotlaringiz bilan IIB Kiberxavfsizlik bo'linmasiga (102 raqamiga yoki "
    "@cyber_102 rasmiy botiga) dadil murojaat qiling.\n\n"
    "2) <b>Siz yolg'iz emassiz</b> — vaziyatni ota-onangizga yoki ishongan kattaga "
    "(ustoz, maktab psixologi) boricha ayting. Kattalarning aralashuvi har qanday "
    "kiber-shantajchini chekinishga majbur qiladi.\n\n"
    "Tinchlandingizmi? 💙"
)


# ============================================================
#  MODUL B — KIBERBULLING SOS ZANJIRI
# ============================================================

BL_START = (
    "🛑 <b>To'xtang</b>, xabarlarni o'qish va javob yozishni hoziroq to'xtating. "
    "Chuqur nafas oling.\n\n"
    "Siz haqingizda yozilayotgan haqoratlar, feyk gaplar yoki masxaralashlar "
    "sizning yomonligingizni anglatmaydi — bu tajovuzkorlarning o'z muammolari va "
    "qo'rqoqligidir. <b>O'z qadringizni ularning so'zlari bilan o'lchamang!</b>\n\n"
    "Quyidagi qadamlarni tartib bilan bosing:"
)

BL_NO_RESPONSE = (
    "🤐 <b>1-QOIDA: TAJOVUZKORLARNI \"BOQMANG\"!</b>\n\n"
    "Bulling qiluvchilarning maqsadi — sizni g'azablantirish va emotsiyaga "
    "yuklashdir. Javob yozganingiz sari ularga yangi qurol berasiz. Eng kuchli "
    "zarba — mutlaq e'tiborsizlik (ignor). Siz jim qolganingizda ular qiziqishini yo'qotadi."
)

BL_COLLECT_FACTS = (
    "📸 <b>2-QOIDA: FAKTLARNI SAQLANG!</b>\n\n"
    "Chatdan chiqib ketishga shoshilmang. Avval sizni haqorat qilgan barcha "
    "xabarlarni va o'sha profillarning aniq linklarini skrinshot qiling. "
    "Tajovuzkorlar xabarni o'chirishi mumkin, ammo saqlangan skrinshotlar ularning aybini isbotlaydi."
)

BL_SHIELD = (
    "🛡 <b>3-QOIDA: RAQAMLI QALQONNI YOQING!</b>\n\n"
    "1) Sizga yozayotgan barcha bezorilarni bloklang.\n"
    "2) Sozlamalarga kirib, notanish odamlar komment yozishi yoki guruhlarga "
    "qo'shishini taqiqlang (konfidentsiallik sozlamalari).\n"
    "3) Guruh adminlariga murojaat qilib, haqoratli postlarni o'chirish va "
    "bezorilarni haydashni talab qiling."
)

BL_LEGAL = (
    "⚖️ <b>HUQUQIY YECHIM:</b>\n\n"
    "1) O'zbekiston Respublikasining Ma'muriy javobgarlik to'g'risidagi kodeksiga "
    "ko'ra, shaxsning sha'ni va qadr-qimmatini haqorat qilish, tuhmat tarqatish "
    "jazolanadi va jarimaga sabab bo'ladi. Internet ortiga yashiringan bezorilarni "
    "Kiberxavfsizlik xodimlari topa oladi.\n\n"
    "2) <b>Yolg'izlikni yeng:</b> agar haqorat qiluvchilar sinfdoshlaring bo'lsa, "
    "bu haqda maktab psixologi, ota-onang yoki sinf rahbaringga ayt. Kattalar va "
    "qonun aralashgan joyda kiberbulling barham topadi.\n\n"
    "<b>Biz har doim siz tomondamiz!</b> 💙"
)


# ============================================================
#  MODUL B — AKKAUNT O'G'IRLASH / SHUBHALI SSILKA (qo'shimcha SOS)
#  Eslatma: bu zanjir topshiriqdagi 3-tugma uchun xuddi shu uslubda
#  tayyorlangan (firibgarlik/fishing bo'yicha).
# ============================================================

AK_START = (
    "🛑 <b>Xotirjam bo'ling.</b> Akkaunt o'g'irlanishi yoki shubhali havola — "
    "tez-tez uchraydigan holat va uni bartaraf etish mumkin.\n\n"
    "Asosiysi — tez harakat qilish. Quyidagi qadamlarni tartib bilan bosing:"
)

AK_PASSWORD = (
    "🔑 <b>1-QOIDA: PAROLLARNI ZUDLIK BILAN O'ZGARTIRING!</b>\n\n"
    "Boshqa qurilmadan (masalan ota-onangiz telefonidan) akkauntingizga kirib, "
    "parolni yangilang. Agar kira olmasangiz — \"Parolni tiklash\" (reset) "
    "funksiyasidan foydalaning. Bir xil parolni boshqa akkauntlarda ishlatgan "
    "bo'lsangiz, ularni ham o'zgartiring."
)

AK_2FA = (
    "🔐 <b>2-QOIDA: IKKI BOSQICHLI HIMOYANI YOQING!</b>\n\n"
    "Sozlamalardan <b>ikki bosqichli tekshiruv (2FA)</b> ni yoqing. Endi hatto "
    "parolni bilgan odam ham telefoningizga kelgan kodsiz kira olmaydi. "
    "Shubhali havolaga (link) bosgan bo'lsangiz — hech qanday kod yoki parol kiritmang!"
)

AK_REPORT = (
    "📣 <b>3-QOIDA: OGOHLANTIRING VA XABAR BERING!</b>\n\n"
    "1) Do'stlaringizga yozing: \"Mening akkauntimdan kelgan shubhali xabar/pul "
    "so'rovlarga ishonmang\".\n"
    "2) O'g'irlangan akkauntni platformaga (Telegram/Instagram) \"shikoyat\" qiling.\n"
    "3) Bank kartangiz ma'lumotlari xavf ostida bo'lsa — bank ilovasidan kartani bloklang."
)

AK_LEGAL = (
    "⚖️ <b>HUQUQIY VA TEXNIK CHORALAR:</b>\n\n"
    "Jinoyat kodeksining 168-moddasi (Firibgarlik), ayniqsa axborot "
    "texnologiyalari orqali sodir etilgani, og'ir jazoni nazarda tutadi. "
    "Raqamli izlar (karta raqami, P2P, IP) o'chmaydi.\n\n"
    "Zudlik bilan chek va skrinshotlar bilan Kiberxavfsizlik markaziga "
    "(102 yoki @cyber_102) murojaat qiling. Voqeani albatta kattalarga ayting!\n\n"
    "<b>Siz to'g'ri harakat qildingiz.</b> 💙"
)


# ============================================================
#  MODUL C — KONSULTATSIYA MATNLARI
# ============================================================

C_MENU = (
    "💬 <b>Anonim maslahat portali</b>\n\n"
    "Qaysi mavzu bo'yicha maslahat kerak? Har biri bo'yicha tayyor "
    "<b>psixologik + yuridik</b> yo'llanma beraman:"
)

C_SHANTAJ = (
    "🧩 <b>KIBER-SHANTAJ: MAJMUAVIY EKSPERT KONSULTATSIYASI</b>\n\n"
    "🧠 <b>PSIXOLOGIK YO'LLANMA:</b> Shantajchining maqsadi sizda aybdorlik va "
    "qo'rquv uyg'otishdir. Siz jinoyat qilmadingiz. Birinchi qoida — emotsional "
    "pauza olish, uning xabarlariga javob yozishni to'xtatish. Yaqinlaringiz sizdan "
    "yuz o'girmaydi, chunki siz manipulyatsiya qurbonisiz.\n\n"
    "⚖️ <b>YURIDIK HIMOYA:</b> Jinoyat kodeksining 165-moddasi (Tovlamachilik) va "
    "141-1-moddasi (Shaxsiy hayot daxlsizligini buzish) bo'yicha sizni qo'rqitayotgan "
    "shaxs jinoiy javobgarlikka tortiladi. Saqlangan skrinshotlar ariza uchun to'liq asos bo'ladi."
)

C_BULLING = (
    "🧩 <b>KIBERBULLING: MAJMUAVIY EKSPERT KONSULTATSIYASI</b>\n\n"
    "🧠 <b>PSIXOLOGIK YO'LLANMA:</b> Onlayn haqorat inson ruhiyatiga zarba beradi; "
    "tajovuzkorlarning maqsadi sizni obro'sizlantirib, o'z kamchiliklarini yopishdir. "
    "O'zingizni ajrating — ularning gaplari shaxsingizni belgilamaydi. Aloqani uzish "
    "(ignor) ularning qurolini zangsizlantiradi.\n\n"
    "⚖️ <b>YURIDIK HIMOYA:</b> Ma'muriy javobgarlik to'g'risidagi kodeksning "
    "41-moddasiga (Haqorat qilish) ko'ra, qasddan kamsitish yirik jarimaga sabab bo'ladi. "
    "Feyk akkauntlar ham raqamli izlar (IP, ID) orqali aniqlanadi. Skrinshotlaringiz "
    "to'liq qonuniy asosdir."
)

C_FRAUD = (
    "🧩 <b>KIBERFIRBGARLIK VA FISHING: MAJMUAVIY EKSPERT KONSULTATSIYASI</b>\n\n"
    "🧠 <b>PSIXOLOGIK YO'LLANMA:</b> Firibgarlar ijtimoiy muhandislikdan foydalanadi — "
    "qiziquvchanlik, shoshqaloqlik yoki yutuq istagini manipulyatsiya qiladi. "
    "O'zingizni ayblamang: professional tuzoqqa katta yoshli, tajribali insonlar ham "
    "tushadi. Buni qimmatli dars sifatida qabul qiling.\n\n"
    "⚖️ <b>YURIDIK VA TEXNIK CHORALAR:</b> Jinoyat kodeksining 168-moddasi (Firibgarlik), "
    "ayniqsa axborot texnologiyalari orqali sodir etilgani, og'ir jazoni nazarda tutadi. "
    "Raqamli izlar (karta raqami, P2P, IP) o'chmaydi. Zudlik bilan bank ilovasidan "
    "kartangizni bloklang va chek hamda skrinshotlar bilan Kiberxavfsizlik markaziga "
    "(102 yoki @cyber_102) murojaat qiling."
)

C_ANON_CHAT_START = (
    "🕊 <b>XAVFSIZ VA ANONIM ALOQA OYNASI</b>\n\n"
    "Bu yerda muammoingizni to'liq yozib qoldirishingiz mumkin.\n\n"
    "🔒 <b>Xavfsizlik kafolati:</b> Telegram profilingiz (ism, username, telefon) "
    "mutaxassisga <b>MUTLAQO KO'RINMAYDI</b>. Tizim sizga maxfiy raqam beradi.\n\n"
    "Sizning maxfiy raqamingiz: <b>{code}</b>\n\n"
    "✍️ Muammoingizni matn yoki audio shaklida shu yerga yozing — navbatchi "
    "psixolog/huquqshunos aynan shu chatga javob yo'llaydi."
)

C_ANON_CHAT_SAVED = (
    "✅ <b>Rahmat! Murojaatingiz qabul qilindi.</b>\n\n"
    "Sizning maxfiy raqamingiz: <b>{code}</b>\n"
    "Navbatchi mutaxassis tez orada javob beradi. Iltimos, sabr qiling — "
    "siz yolg'iz emassiz. 💙"
)
