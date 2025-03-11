from flask import Flask, request
from aiogram import Bot, Dispatcher, types, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

# ✅ توكن البوت مباشر
TOKEN = "7803240855:AAEKbgY2IV3WOETp12oCtt5d-Hvl42mWDpU"

# ✅ تهيئة البوت و Dispatcher
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

# ✅ إعداد لوحة الأزرار
keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="📜 التعليمات")],
        [types.KeyboardButton(text="🖨️ أريد طباعة ملفاتي"), types.KeyboardButton(text="📄 أوراق عمل مطبوعة")],
        [types.KeyboardButton(text="💻 أوراق عمل رقمية"), types.KeyboardButton(text="📅 حجز لقاء استشاري أونلاين")],
        [types.KeyboardButton(text="✉️ التواصل مع الإدارة"), types.KeyboardButton(text="🎟️ تطبيق أكواد الخصم")]
    ],
    resize_keyboard=True
)

# ✅ الردود الجاهزة
responses = {
    "📜 التعليمات": "قوانين الجروب...",
    "🖨️ أريد طباعة ملفاتي": "رابط الطباعة: https://t.me/yaacolor/39",
    "📄 أوراق عمل مطبوعة": "رابط: https://t.me/yaacolor/38",
    "💻 أوراق عمل رقمية": "رابط: https://t.me/yaacolor/38",
    "📅 حجز لقاء استشاري أونلاين": "https://t.me/yaacolor/37",
    "✉️ التواصل مع الإدارة": "https://t.me/G_Coordinator",
    "🎟️ تطبيق أكواد الخصم": "https://t.me/yaacolor/36"
}

# ✅ التعامل مع أمر /start
@router.message(lambda msg: msg.text == "/start")
async def start(message: types.Message):
    await message.answer("👋 أهلاً بك في بوت ياا ملون! اختر من القائمة:", reply_markup=keyboard)

# ✅ التعامل مع الرسائل النصية
@router.message(lambda msg: msg.text in responses.keys())
async def reply(message: types.Message):
    await message.answer(responses[message.text])

# ✅ إعداد Flask
app = Flask(__name__)

# ✅ استقبال Webhook من تيليجرام
@app.route('/' + TOKEN, methods=['POST'])
def receive_update():
    update = types.Update(**request.json)
    asyncio.create_task(dp.feed_update(bot, update))  # إرسال التحديث للباكند
    return "ok", 200

# ✅ صفحة رئيسية للتأكد أن البوت يعمل
@app.route('/')
def index():
    return "✅ البوت يعمل بنجاح!", 200
