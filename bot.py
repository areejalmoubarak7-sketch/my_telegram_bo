import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# --- جزء السيرفر الوهمي لإرضاء Render ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Running!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

# تشغيل السيرفر في خلفية البوت
threading.Thread(target=run_server, daemon=True).start()
# ---------------------------------------

TOKEN = os.getenv("TOKEN")

LECTURES_DATA = {
    "📂 خوارزميات 1": "https://drive.google.com/drive/folders/15WH86GfNYOn0kq489y3sGkzNvJpIyWcX?usp=drive_link",
    "🔢 التحليل العددي": "https://drive.google.com/drive/folders/1eL-cRjjYDiY-c1oEG0dZQIjGTh3QiiBC?usp=drive_link",
    "🚀 خوارزميات متقدمة": "https://drive.google.com/drive/folders/1_v0DaeCcI7Ze_Scw4vBJYCf62Ak0a07-?usp=drive_link",
    "☕ برمجة متقدمة (جافا)": "https://drive.google.com/drive/folders/1Owok6FJgYOkkY96iQN5ZGpX_Ptf78IAq?usp=drive_link",
    "📘 برمجة 1": "https://drive.google.com/drive/folders/15WH86GfNYOn0kq489y3sGkzNvJpIyWcX?usp=drive_link",
    "📐 رياضيات 2": "https://drive.google.com/drive/folders/1IFRKrR-gz99RhttfgxafL6cSaOKk7qTU?usp=drive_link"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📂 خوارزميات 1", "🔢 التحليل العددي"],
        ["🚀 خوارزميات متقدمة", "☕ برمجة متقدمة (جافا)"],
        ["📘 برمجة 1", "📐 رياضيات 2"],
        ["🎓 الكورسات", "🟢 جروب الواتساب"],
        ["👩‍🏫 تواصل مع المهندسة"],
        ["🤖 بوت التواصل", "🛠️ بوت الإدارة"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    welcome_text = "🎓 أهلاً بك في بوت محاضرات الشهباء\n\nاختر المادة من الأزرار 👇"
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    if user_text in LECTURES_DATA:
        url = LECTURES_DATA[user_text]
        inline_kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 فتح المجلد", url=url)]])
        await update.message.reply_text(f"✅ مادة {user_text}:", reply_markup=inline_kb)
    elif user_text == "🟢 جروب الواتساب":
        await update.message.reply_text("https://chat.whatsapp.com/D5LQhEqx2rZ9G5InsHSw5v")
    # ... بقية الأزرار تعمل بنفس الطريقة

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
    app.run_polling()