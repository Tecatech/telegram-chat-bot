from telethon import events
from telethon.tl.custom import Message
from telethon.tl.types import InputMediaDice

from app import bot

@bot.on(events.ChatAction(func = lambda e: e.is_group and e.user_added and e.user_id == bot.me.id))
async def on_join(event: events.ChatAction.Event):
    await event.respond('Здравствуйте, Барышни и Господа!')

@bot.on(events.NewMessage(func = lambda e: e.text.lower() == '/ball'))
async def send_ball(event: Message):
    await bot.send_message(event.chat.id, file = InputMediaDice('🏀'))