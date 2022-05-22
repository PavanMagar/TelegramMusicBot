from pyrogram import Client
from Codexun.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from Codexun.config import (
    BOT_USERNAME,
)

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hey, this is the assistant of music bot, if you want to make your own music bot then visit at @TeamCodexun and contact us!\n\nPowered by @Codexun")
  return
