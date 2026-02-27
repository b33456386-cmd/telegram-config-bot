from telegram import Bot

TOKEN = "8478830916:AAEEnX4qCVq7hFk_PC2mtxEa14JlLg1z78s"
CHANNEL_ID = "@beniiiba"

bot = Bot(token=TOKEN)

try:
    bot.send_message(chat_id=CHANNEL_ID, text="تست 🚀")
    print("ارسال شد")
except Exception as e:
    print("خطا:", e)
