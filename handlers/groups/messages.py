from aiogram import Router, F
from aiogram.types import Message

group_message_router = Router()

@group_message_router.message(F.chat.type == "group" or F.chat.type == "supergroup")
async def handle_group_message(message: Message):
    await message.answer("This is a group message handler.")