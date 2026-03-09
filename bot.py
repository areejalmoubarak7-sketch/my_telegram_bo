import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# إعداد السجلات لمتابعة البوت
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# التوكن الخاص بكِ
TOKEN = "8337883589:AAGkLauWquB5wNUzH6vvqpmrF7WaT5kzWSs"

# --- القائمة الرئيسية ---
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📚 المحاضرات (المستويات)", callback_data="lectures")],
        [InlineKeyboardButton("📢 قناة التلغرام الجديدة", url="https://t.me/+kL4uo25MCKoyY2I0")],
        [InlineKeyboardButton("🟢 قناة الواتساب الرسمية", url="https://chat.whatsapp.com/D5LQhEqx2rZ9G5InsHSw5v?mode=gi_t")],
        [InlineKeyboardButton("🎓 الكورسات التدريبية", callback_data="courses")],
        [InlineKeyboardButton("📞 تواصل شخصي مع المهندسة", callback_data="contact")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بكم في منصة المهندسة أريج المبارك التعليمية.\n\n"
        "يمكنكم الوصول للمحاضرات، الانضمام لقنواتنا، أو التواصل معي مباشرة عبر الأزرار أدناه:",
        reply_markup=main_menu_keyboard()
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # قسم المحاضرات
    if data == "lectures":
        keyboard = [
            [InlineKeyboardButton("المستوى الأول", callback_data="level1")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="back")]
        ]
        await query.edit_message_text("📚 اختر المستوى الدراسي:", reply_markup=InlineKeyboardMarkup(keyboard))

    # روابط المواد (برمجة 1 ورياضيات 2)
    elif data == "level1":
        keyboard = [
            [InlineKeyboardButton("💻 برمجة 1", url="https://drive.google.com/drive/folders/1sr1h4Xa0dAj76RHjDHhraFy_DrYG5obu")],
            [InlineKeyboardButton("📐 الرياضيات 2", url="https://drive.google.com/drive/folders/1IFRKrR-gz99RhttfgxafL6cSaOKk7qTU")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="lectures")]
        ]
        await query.edit_message_text("📚 مواد المستوى الأول المتاحة حالياً:", reply_markup=InlineKeyboardMarkup(keyboard))

    # قسم التواصل الشخصي المحدث
    elif data == "contact":
        keyboard = [
            [InlineKeyboardButton("💬 تلغرام: @Areej_almoubarak", url="https://t.me/Areej_almoubarak")],
            [InlineKeyboardButton("🟢 واتساب: 0930011207", url="https://wa.me/963930011207")],
            [InlineKeyboardButton("🟢 واتساب: 0996499901", url="https://wa.me/963996499901")],
            [InlineKeyboardButton("🔙 رجوع للقائمة الرئيسية", callback_data="back")]
        ]
        await query.edit_message_text(
            "📞 يسعدني تواصلكم الشخصي للاستفسارات البرمجية والأكاديمية عبر:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "courses":
        keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
        await query.edit_message_text("🎓 قسم الكورسات قيد التجهيز، سيتم الإعلان عنه قريباً.", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "back":
        await query.edit_message_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    
    print("Bot is updating and running successfully...")
    application.run_polling()