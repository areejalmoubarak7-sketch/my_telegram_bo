import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# إعداد السجلات (Logs) لمتابعة أي أخطاء تظهر في Railway
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# التوكن الخاص بكِ (تأكدي من تغييره لاحقاً للأمان)
TOKEN = "8337883589:AAF3KPvdj5XggUE60CnOo90cMzy2T0S6cuc"

# رسالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 المحاضرات", callback_data="lectures")],
        [InlineKeyboardButton("🎓 الكورسات", callback_data="courses")],
        [InlineKeyboardButton("🤖 الذكاء الاصطناعي", callback_data="ai")],
        [InlineKeyboardButton("📞 تواصل معنا", callback_data="contact")]
    ]

    await update.message.reply_text(
        "👋 مرحباً بكم\n\n"
        "معكم المهندسة أريج المبارك.\n"
        "جاهزة لمساعدتكم بكل ما يخص مواد الهندسة المعلوماتية.\n\n"
        "اختر من القائمة:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# معالجة الضغط على الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # قائمة المحاضرات
    if data == "lectures":
        keyboard = [
            [InlineKeyboardButton("المستوى الأول", callback_data="level1")],
            [InlineKeyboardButton("المستوى الثاني", callback_data="level2")],
            [InlineKeyboardButton("المستوى الثالث", callback_data="level3")],
            [InlineKeyboardButton("المستوى الرابع", callback_data="level4")],
            [InlineKeyboardButton("المستوى الخامس", callback_data="level5")],
            [InlineKeyboardButton("📤 ساهم بمحاضرات المادة", callback_data="upload")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="back")]
        ]
        await query.edit_message_text("📚 اختر المستوى:", reply_markup=InlineKeyboardMarkup(keyboard))

    # المستوى الأول (ملاحظة: الروابط يجب أن تبدأ بـ https://)
    elif data == "level1":
        keyboard = [
            [InlineKeyboardButton("برمجة 1", url="https://t.me/example")],
            [InlineKeyboardButton("برمجة 2", url="https://t.me/example")],
            [InlineKeyboardButton("الرياضيات 1", url="https://t.me/example")],
            [InlineKeyboardButton("الرياضيات 2", url="https://t.me/example")],
            [InlineKeyboardButton("المحاسبة المالية 1", url="https://t.me/example")],
            [InlineKeyboardButton("اساسيات الادارة", url="https://t.me/example")],
            [InlineKeyboardButton("الحضارة العربية", url="https://t.me/example")],
            [InlineKeyboardButton("اللغة الانكليزية 1", url="https://t.me/example")],
            [InlineKeyboardButton("اللغة الانكليزية 2", url="https://t.me/example")],
            [InlineKeyboardButton("اخلاقيات المهنة", url="https://t.me/example")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="lectures")]
        ]
        await query.edit_message_text("📚 مواد المستوى الأول:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data in ["level2", "level3", "level4", "level5"]:
        keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="lectures")]]
        await query.edit_message_text("📚 سيتم إضافة تفاصيل المواد خلال أسبوع إن شاء الله.", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "upload":
        keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="lectures")]]
        await query.edit_message_text("📤 إذا أردت المساهمة بمحاضرات الطلاب\n\nارفع الملفات هنا:\n(ضع رابط الرفع هنا)", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "courses":
        keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
        await query.edit_message_text("🎓 قسم الكورسات سيتم إضافته قريباً.", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "ai":
        keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
        await query.edit_message_text("🤖 سيتم إضافة قسم لتعلم الذكاء الاصطناعي قريباً.", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "contact":
        keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
        await query.edit_message_text("📞 للتواصل:\n(ضع هنا رابط تلغرام أو واتساب)", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "back":
        keyboard = [
            [InlineKeyboardButton("📚 المحاضرات", callback_data="lectures")],
            [InlineKeyboardButton("🎓 الكورسات", callback_data="courses")],
            [InlineKeyboardButton("🤖 الذكاء الاصطناعي", callback_data="ai")],
            [InlineKeyboardButton("📞 تواصل معنا", callback_data="contact")]
        ]
        await query.edit_message_text("القائمة الرئيسية:", reply_markup=InlineKeyboardMarkup(keyboard))

# تشغيل البوت
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    
    print("Bot is running...")
    application.run_polling()