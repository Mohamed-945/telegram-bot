# set_webhook.py
import asyncio
from telegram_bot import bot

async def setup_webhook():
    webhook_url = "https://telegram-bot.onrender.com/7803240855:AAEKbgY2IV3WOETp12oCtt5d-Hvl42mWDpU"
    await bot.set_webhook(webhook_url)
    print("✅ Webhook Set Successfully!")

if __name__ == "__main__":
    asyncio.run(setup_webhook())
