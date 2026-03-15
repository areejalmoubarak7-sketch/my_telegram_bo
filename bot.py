import os
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# جلب التوكن من إعدادات Render
TOKEN = os.getenv("TOKEN")

# قائمة المواد والروابط
LECTURES_DATA = {
    "📂 خوارزميات 1": "https://drive.google.com/drive/folders/15WH86GfNYOn0kq489y3sGkzNvJpIyWcX?usp=drive_link",
    "🔢 التحليل العددي": "https://drive.google.com/drive/folders/1eL-cRjjYDiY-c1oEG0dZQIjGTh3QiiBC?usp=drive_link",
    "🚀 خوارزميات متقدمة": "https://drive.google.com/drive/folders/1_v0DaeCcI7Ze_Scw4vBJYCf62Ak0a07-?usp=drive_link",
    "☕ برمجة متقدمة (جافا)": "https://drive.google.com/drive/folders/1Owok6FJgYOkkY96iQN5ZGpX_Ptf78IAq?usp=drive_link",
    "📘 برمجة 1": "https://drive.google.com/drive/folders/15WH86GfNYOn0kq489y3sGkzNvJpIyWcX?usp=drive_link",
    "📐 رياضيات 2": "https://drive.google.com/drive/folders/1IFRKrR-gz99RhttfgxafL6cSaOKk7qTU?usp=drive_link"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إعداد لوحة المفاتيح
    keyboard = [
        ["📂 خوارزميات 1", "🔢 التحليل العددي"],
        ["🚀 خوارزميات متقدمة", "☕ برمجة متقدمة (جافا)"],
        ["📘 برمجة 1", "📐 رياضيات 2"],
        ["🎓 الكورسات", "🟢 جروب الواتساب"],
        ["👩‍🏫 تواصل مع المهندسة"],
        ["🤖 بوت التواصل", "🛠️ بوت الإدارة"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    # رسالة ترحيبية مبسطة لتجنب أخطاء التنسيق (Parse Errors)
    welcome_text = (
        "🎓 أهلاً بك في بوت محاضرات الشهباء\n\n"
        "هنا تجد كل ما يهمك من محاضرات وروابط تواصل:\n\n"
        "📢 قناتنا على تلغرام: t.me/ITEAcademic\n"
        "💬 مجموعة الواتساب: https://chat.whatsapp.com/D5LQhEqx2rZ9G5InsHSw5v\n\n"
        "اختر المادة أو الخدمة من الأزرار أدناه 👇"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    # معالجة روابط المواد
    if user_text in LECTURES_DATA:
        url = LECTURES_DATA[user_text]
        inline_kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 فتح المجلد", url=url)]])
        await update.message.reply_text(f"✅ مادة {user_text}:\nتفضل الرابط المطلوب:", reply_markup=inline_kb)

    # زر الواتساب
    elif user_text == "🟢 جروب الواتساب":
        whatsapp_url = "https://chat.whatsapp.com/D5LQhEqx2rZ9G5InsHSw5v"
        inline_kb = InlineKeyboardMarkup([[InlineKeyboardButton("الانضمام للواتساب", url=whatsapp_url)]])
        await update.message.reply_text("تفضل رابط الانضمام لمجموعة الواتساب الخاصة بنا:", reply_markup=inline_kb)

    # الكورسات
    elif user_text == "🎓 الكورسات":
        await update.message.reply_text("📚 الكورسات المتوفرة حالياً:\n\n- كورس البرمجة\n- كورس الخوارزميات\n\nللتسجيل تواصل مع الإدارة.")

    # روابط التواصل
    elif user_text == "👩‍🏫 تواصل مع المهندسة":
        inline_kb = InlineKeyboardMarkup([[InlineKeyboardButton("ارسل رسالة", url="https://t.me/ITE_eng")]])
        await update.message.reply_text("يمكنك التواصل مع المهندسة مباشرة من هنا:", reply_markup=inline_kb)

    elif user_text == "🤖 بوت التواصل":
        inline_kb = InlineKeyboardMarkup([[InlineKeyboardButton("فتح البوت", url="https://t.me/Contact_ITE_Bot")]])
        await update.message.reply_text("بوت التواصل الرسمي:", reply_markup=inline_kb)

    elif user_text == "🛠️ بوت الإدارة":
        inline_kb = InlineKeyboardMarkup([[InlineKeyboardButton("فتح البوت", url="https://t.me/Admin_ITE_Bot")]])
        await update.message.reply_text("بوت الإدارة للأمور التنظيمية:", reply_markup=inline_kb)

    else:
        await update.message.reply_text("⚠️ يرجى اختيار مادة أو خدمة من الأزرار الظاهرة.")

if __name__ == '__main__':
    if not TOKEN:
        print("❌ Error: TOKEN variable is not set in Environment Variables!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
        
        print("🚀 البوت جاهز ويعمل الآن...")
        app.run_polling()