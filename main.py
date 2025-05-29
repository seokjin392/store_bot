from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("안녕하세요! 입점 절차 안내를 도와드릴게요.")

app = ApplicationBuilder().token("8050769215:AAEz-RNFAgEMP8sEcVMuIlZt5rirZ61exaM").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
