import asyncio
from aiogram import Bot

TOKEN = "7803240855:AAEKbgY2IV3WOETp12oCtt5d-Hvl42mWDpU"
WEBHOOK_URL = "https://telegram-bot-c2uv.onrender.com/7803240855:AAEKbgY2IV3WOETp12oCtt5d-Hvl42mWDpU"  # ✅ رابط صحيح مع التوكن

bot = Bot(token=TOKEN)

async def set_webhook():
    await bot.set_webhook(WEBHOOK_URL)
    print("✅ Webhook تم ضبطه بنجاح!")

if __name__ == "__main__":
    asyncio.run(set_webhook())
