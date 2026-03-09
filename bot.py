import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# إعداد السجلات لمراقبة أداء البوت في Railway
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# التوكن الخاص بكِ
TOKEN = "8337883589:AAF3KPvdj5XggUE60CnOo90cMzy2T0S6cuc"

# --- القائمة الرئيسية ---
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📚 المحاضرات (المستويات)", callback_data="lectures")],
        [InlineKeyboardButton("📢 قناة التلغرام", url="https://t.me/Areej_almoubarak")],
        [InlineKeyboardButton("🎓 الكورسات", callback_data="courses")],
        [InlineKeyboardButton("🤖 الذكاء الاصطناعي", callback_data="ai")],
        [InlineKeyboardButton("📞 تواصل معنا", callback_data="contact")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بكم في منصة المهندسة أريج المبارك التعليمية.\n\n"
        "أنا هنا لمساعدتكم في الوصول للمحاضرات والكورسات البرمجية.\n"
        "اختر ما تبحث عنه من الأزرار أدناه:",
        reply_markup=main_menu_keyboard()
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # قسم المحاضرات والمستويات
    if data == "lectures":
        keyboard = [
            [InlineKeyboardButton("المستوى الأول", callback_data="level1")],
            [InlineKeyboardButton("بقية المستويات (قريباً)", callback_data="back")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="back")]
        ]
        await query.edit_message_text("📚 اختر المستوى الدراسي:", reply_markup=InlineKeyboardMarkup(keyboard))

    # روابط المواد المحددة
    elif data == "level1":
        keyboard = [
            [InlineKeyboardButton("💻 برمجة 1", url="https://drive.google.com/drive/folders/1sr1h4Xa0dAj76RHjDHhraFy_DrYG5obu")],
            [InlineKeyboardButton("📐 الرياضيات 2", url="https://drive.google.com/drive/folders/1IFRKrR-gz99RhttfgxafL6cSaOKk7qTU")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="lectures")]
        ]
        await query.edit_message_text("📚 مواد المستوى الأول المتاحة حالياً:", reply_markup=InlineKeyboardMarkup(keyboard))

    # قسم التواصل مع الأرقام السورية المحدثة
    elif data == "contact":
        # روابط واتساب مباشرة للأرقام السورية التي زودتني بها
        wa_link1 = "https://wa.me/963930011207"
        wa_link2 = "https://wa.me/963996499901"
        tg_link = "https://t.me/Areej_almoubarak"

        keyboard = [
            [InlineKeyboardButton("💬 تلغرام: أريج المبارك", url=tg_link)],
            [InlineKeyboardButton("🟢 واتساب (الرقم الأول)", url=wa_link1)],
            [InlineKeyboardButton("🟢 واتساب (الرقم الثاني)", url=wa_link2)],
            [InlineKeyboardButton("🔙 رجوع", callback_data="back")]
        ]
        await query.edit_message_text("📞 يسعدنا تواصلكم عبر الوسائل التالية:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data in ["courses", "ai"]:
        keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
        await query.edit_message_text("🚧 هذا القسم قيد التطوير وسيتم تفعيله قريباً.", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "back":
        await query.edit_message_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    
    print("Bot is updating and running...")
    application.run_polling()