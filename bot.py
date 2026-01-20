import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ciao 🤍\n"
        "Sono il bot di supporto.\n\n"
        "Se non riesci a contattare gli admin, sei nel posto giusto.\n"
        "Scrivimi cosa è successo e ti aiuto volentieri 😊"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ti sto leggendo 💬\n"
        "Raccontami meglio, sono qui per aiutarti."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.run_polling()
