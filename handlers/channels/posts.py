from aiogram import Router, F
from aiogram.types import Message

channel_post_router = Router()

@channel_post_router.message(F.chat.type == "channel")
async def handle_channel_post(message: Message):
    await message.answer("This is a channel post handler.")
