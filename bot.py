import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я умный бот с ИИ! Задай мне любой вопрос!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = model.generate_content(user_message)
    await update.message.reply_text(response.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))
app.run_polling()
```

Сохрани и в cmd на компьютере:
```
cd C:\projects\mybot
git add .
git commit -m "add gemini ai"
git push