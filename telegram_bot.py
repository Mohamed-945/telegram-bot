from flask import Flask, request
from aiogram import Bot, Dispatcher, types, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os
from aiogram import F

# إعداد البوت
TOKEN = "7803240855:AAEKbgY2IV3WOETp12oCtt5d-Hvl42mWDpU"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

# لوحة الأزرار
keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="📜 التعليمات")],
        [types.KeyboardButton(text="🖨️ أريد طباعة ملفاتي"), types.KeyboardButton(text="📄 أوراق عمل مطبوعة")],
        [types.KeyboardButton(text="💻 أوراق عمل رقمية"), types.KeyboardButton(text="📅 حجز لقاء استشاري أونلاين")],
        [types.KeyboardButton(text="✉️ التواصل مع الإدارة"), types.KeyboardButton(text="🎟️ تطبيق أكواد الخصم")]
    ],
    resize_keyboard=True
)

# الردود الجاهزة
responses = {
    "📜 التعليمات": "قوانين الجروب...",
    "🖨️ أريد طباعة ملفاتي": "رابط الطباعة: https://t.me/yaacolor/39",
    "📄 أوراق عمل مطبوعة": "رابط: https://t.me/yaacolor/38",
    "💻 أوراق عمل رقمية": "رابط: https://t.me/yaacolor/38",
    "📅 حجز لقاء استشاري أونلاين": "https://t.me/yaacolor/37",
    "✉️ التواصل مع الإدارة": "https://t.me/G_Coordinator",
    "🎟️ تطبيق أكواد الخصم": "https://t.me/yaacolor/36"
}

# التعامل مع /start
@router.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer("👋 أهلاً بك في بوت ياا ملون!", reply_markup=keyboard)

@router.message(F.text.in_(responses.keys()))
async def reply(message: types.Message):
    await message.answer(responses[message.text])

# Flask app
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def receive_update():
    update = types.Update(**request.json)
    asyncio.create_task(dp.feed_update(bot, update))
    return "ok"

@app.route('/')
def index():
    return "البوت يعمل!"

# إعداد Webhook
async def setup_webhook():
    webhook_url = f"https://telegram-bot.onrender.com/{TOKEN}"  
    await bot.set_webhook(webhook_url)

# تشغيل التطبيق
if __name__ == '__main__':
    asyncio.run(setup_webhook())  # إعداد الـ webhook
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
