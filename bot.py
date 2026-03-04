from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 1. ضع التوكن الجديد هنا (الذي حصلت عليه بعد عمل Revoke)
TOKEN = "8337883589:AAGSNrZhtc8oW-o8A9SikB5FQ6S3N-5ipVo"

# 2. قائمة المواد والروابط (تعدلها بسهولة من هنا)
LECTURES_DATA = {
    "📘 برمجة 1": "https://example.com/prog1",
    "📗 رياضيات 1": "https://example.com/math1",
    "🌐 شبكات": "https://example.com/net",
    "💻 نظم تشغيل": "https://example.com/os"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إنشاء الأزرار: كل قائمة داخلية [ ] هي سطر في الكيبورد
    keyboard = [
        ["📘 برمجة 1", "📗 رياضيات 1"],
        ["🌐 شبكات", "💻 نظم تشغيل"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "👋 أهلاً بك! اختر المادة التي تبحث عن محاضراتها:",
        reply_markup=reply_markup
    )

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    if user_text in LECTURES_DATA:
        url = LECTURES_DATA[user_text]
        await update.message.reply_text(f"🔗 رابط محاضرات {user_text}:\n{url}")
    else:
        await update.message.reply_text("⚠️ من فضلك اختر مادة من الأزرار الظاهرة في الأسفل.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
    
    print("✅ البوت شغال وجاهز لاستلام الطلبات...")
    app.run_polling()