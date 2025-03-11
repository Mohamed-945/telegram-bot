import asyncio
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

TOKEN = "7803240855:AAEKbgY2IV3WOETp12oCtt5d-Hvl42mWDpU"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

async def setup():
    webhook_url = f"https://telegram-bot.onrender.com/{TOKEN}"  # تأكد من الرابط الصحيح
    await bot.set_webhook(webhook_url)
    print(f"✅ Webhook تم ضبطه: {webhook_url}")

if __name__ == '__main__':
    asyncio.run(setup())
