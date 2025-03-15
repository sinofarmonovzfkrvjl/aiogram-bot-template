from aiogram import Router, F
from aiogram.types import Message
from data import ADMIN_ID

admin_router = Router()

@admin_router.message(F.chat.id == ADMIN_ID)
async def admin_handler(message: Message):
    await message.answer("Salom Admin")