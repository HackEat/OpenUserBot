#COPYRIGHT © 2020 FLIXTEAM
#Module Developed By @RandomGuyRG69 
#Feel Free To Modify It With Credits.

import io
import math
import urllib.request
from os import remove
import random
from telethon import events
from userbot import bot
from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event

#Replies With A Random Quote From Animes.

QUOTES = [
    "I love heroes, but I don't want to be one. Do you even know what a hero is!? For example, you have some meat. Pirates will feast on the meat, but the hero will distribute it among the people! I want to eat the meat! \n- Monkey D. Luffy",
    "If you lose credibility by just admitting fault, then you didn’t have any in the first place.\n – Fujitora",
    "You need to accept the fact that you’re not the best and have all the will to strive to be better than anyone you face.\n – Roronoa Zoro",
    "When I decided to follow my dream, I had already discarded my life.\n – Roronoa Zoro",
    "There is someone that I must meet again. And until that day…not even Death itself can take my life away!\n – Roronoa Zoro",
    "No matter how deep the night, it always turns to day, eventually.\n – One Piece",
    "It may be hard right now but you must silent those thoughts. Stop counting those things you have lost, what is gone is gone. So ask yourself, what is there that still remains to you.\n – One Piece",
    "Moving on doesn’t mean you forget about things. It just means you have to accept what’s happened and continue living.\n – Erza Scarlet",
    "Hurt me with the truth. But never comfort me with a lie.\n – Erza Scarlet",
    "If you don’t take risks, you can’t create a future.\n – Monkey D. Luffy ",
    "If you believe in your dreams, I will prove to you, that you can achieve your dreams just by working hard.\n – Rock Lee",
]

@register(outgoing=True, pattern="^.quote$")
async def quote(msgs):
    """ For .quote command, check if the bot is running.  """
    await msgs.edit(f"{random.choice(QUOTES)}")
                     

CMD_HELP.update({
    "quotes":
    ".quote\
\nUsage: Type .quote To Get A Random Quote From Animes."
})
