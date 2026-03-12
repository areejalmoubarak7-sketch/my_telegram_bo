from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 1. ضع التوكن الجديد هنا
TOKEN = "8337883589:AAFlCa2c4WWybGET5KJEGkVBLsHK6l6qFc4"

# 2. تحديث قائمة المواد والروابط الجديدة
LECTURES_DATA = {
    "📂 خوارزميات 1": "https://drive.google.com/drive/folders/15WH86GfNYOn0kq489y3sGkzNvJpIyWcX?usp=drive_link",
    "🔢 التحليل العددي": "https://drive.google.com/drive/folders/1eL-cRjjYDiY-c1oEG0dZQIjGTh3QiiBC?usp=drive_link",
    "🚀 خوارزميات متقدمة": "https://drive.google.com/drive/folders/1_v0DaeCcI7Ze_Scw4vBJYCf62Ak0a07-?usp=drive_link",
    "☕ برمجة متقدمة (جافا)": "https://drive.google.com/drive/folders/1Owok6FJgYOkkY96iQN5ZGpX_Ptf78IAq?usp=drive_link"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إنشاء أزرار المواد
    keyboard = [
        ["📂 خوارزميات 1", "🔢 التحليل العددي"],
        ["🚀 خوارزميات متقدمة", "☕ برمجة متقدمة (جافا)"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    # رسالة ترحيبية مع رابط القناة
    welcome_text = (
        "🎓 أهلاً بك في بوت المواد الجامعية ITE\n\n"
        "يمكنك الحصول على روابط المحاضرات بالضغط على الأزرار أدناه.\n\n"
        "📢 تابع آخر التحديثات على قناتنا:\n"
        "https://t.me/ITEAcademic"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, disable_web_page_preview=True)

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    if user_text in LECTURES_DATA:
        url = LECTURES_DATA[user_text]
        # إرسال الرابط مع زر "فتح الرابط" بشكل احترافي
        inline_kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 فتح المجلد", url=url)]])
        await update.message.reply_text(
            f"✅ تفضل، رابط مجلد {user_text}:",
            reply_markup=inline_kb
        )
    else:
        await update.message.reply_text("⚠️ يرجى اختيار مادة من الأزرار الظاهرة في الأسفل.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
    
    print("✅ البوت شغال الآن مع المواد الجديدة...")
    app.run_polling()