from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import pytesseract
from PIL import Image

التوكن الخاص بك
TOKEN = "6095098175:AAEpdMXWPON43lR0OvgDFhUooBfp5DV9qsA"

تعريف البوت مع إعدادات اتصال مخففة لتجاوز الخطأ
def run_bot():
app = ApplicationBuilder().token(TOKEN).build()

# دالة بسيطة للرد
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text("البوت يعمل يا مهندس علي!")

app.add_handler(MessageHandler(filters.ALL, echo))
print("جاري تشغيل البوت... إذا ظهر خطأ فهذا يعني أن شبكتك تحجب الوصول.")
app.run_polling()

if name == 'main':
run_bot()
