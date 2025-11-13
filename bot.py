import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен твоего бота (замени на свой, копируй без лишних пробелов/кавычек)
TOKEN = "8154930923:AAFMv8f6p_bla_At8tadSjARGubXxTps7-4"

# Список заданий
TASKS = [
    "Спой песню как робот 🤖",
    "Спой куплет шёпотом 😶",
    "Танцуй, пока поёшь 💃",
    "Исполни песню как рок-звезда 🎸",
    "Пой с выражением грусти 😢",
    "Пой, как будто ты в Голливуде 🌟",
    "Изобрази драму из песни 🎭",
    "Пой стоя на одной ноге 🦩",
    "Спой как рэпер, даже если это не рэп 🎤",
    "Пой, начиная каждое слово с буквы «М» 😆"
]

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎲 Новое задание", callback_data="new_task")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я караоке-бот 🎤\nНажми кнопку, чтобы получить задание:",
        reply_markup=reply_markup
    )

# callback при нажатии кнопки
async def new_task_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    task = random.choice(TASKS)
    keyboard = [[InlineKeyboardButton("🎲 Ещё задание", callback_data="new_task")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"👉 Твое задание:\n\n{task}",
        reply_markup=reply_markup
    )

# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(new_task_callback, pattern="new_task"))
    print("✅ Бот запущен! Нажми Ctrl+C, чтобы остановить.")
    app.run_polling()
