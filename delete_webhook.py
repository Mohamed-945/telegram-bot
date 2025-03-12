import asyncio
from aiogram import Bot

TOKEN = "7803240855:AAEKbgY2IV3WOETp12oCtt5d-Hvl42mWDpU"  # ضع التوكن الصحيح

bot = Bot(token=TOKEN)

async def delete_webhook():
    await bot.delete_webhook(drop_pending_updates=True)
    print("✅ Webhook تم حذفه بنجاح!")

if __name__ == "__main__":
    asyncio.run(delete_webhook())

