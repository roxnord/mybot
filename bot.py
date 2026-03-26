from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8761303931:AAGf_jiyabgJbzlUCZd0qdRfR6SLpWwKb7A"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой первый бот!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    if message == "привет":
        await update.message.reply_text("Привет! Как дела?")
    elif message == "пока":
        await update.message.reply_text("До свидания!")
    else:
        await update.message.reply_text("Я не понимаю тебя")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))
app.run_polling()
