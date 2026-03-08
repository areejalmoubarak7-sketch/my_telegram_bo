from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("T8337883589:AAGSNrZhtc8oW-o8A9SikB5FQ6S3N-5ipVo")

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

        await query.edit_message_text(
            "📚 اختر المستوى:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # المستوى الأول
    elif data == "level1":

        keyboard = [
            [InlineKeyboardButton("برمجة 1", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("برمجة 2", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("الرياضيات 1", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("الرياضيات 2", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("المحاسبة المالية 1", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("اساسيات الادارة", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("الحضارة العربية", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("اللغة الانكليزية 1", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("اللغة الانكليزية 2", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("اخلاقيات المهنة", url="PUT_LINK_HERE")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="lectures")]
        ]

        await query.edit_message_text(
            "📚 مواد المستوى الأول:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # المستويات الأخرى
    elif data in ["level2", "level3", "level4", "level5"]:

        await query.edit_message_text(
            "📚 سيتم إضافة تفاصيل المواد خلال أسبوع إن شاء الله."
        )

    # رفع المحاضرات
    elif data == "upload":

        await query.edit_message_text(
            "📤 إذا أردت المساهمة بمحاضرات الطلاب\n\n"
            "ارفع الملفات هنا:\n"
            "ضع رابط Google Drive أو نموذج الرفع هنا"
        )

    # الكورسات
    elif data == "courses":

        await query.edit_message_text(
            "🎓 قسم الكورسات سيتم إضافته قريباً."
        )

    # الذكاء الاصطناعي
    elif data == "ai":

        await query.edit_message_text(
            "🤖 سيتم إضافة قسم لتعلم الذكاء الاصطناعي قريباً."
        )

    # التواصل
    elif data == "contact":

        await query.edit_message_text(
            "📞 للتواصل:\n"
            "ضع هنا رابط تلغرام أو واتساب."
        )

    # رجوع
    elif data == "back":

        keyboard = [
            [InlineKeyboardButton("📚 المحاضرات", callback_data="lectures")],
            [InlineKeyboardButton("🎓 الكورسات", callback_data="courses")],
            [InlineKeyboardButton("🤖 الذكاء الاصطناعي", callback_data="ai")],
            [InlineKeyboardButton("📞 تواصل معنا", callback_data="contact")]
        ]

        await query.edit_message_text(
            "القائمة الرئيسية:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()