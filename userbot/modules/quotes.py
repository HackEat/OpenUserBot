import io
import math
import urllib.request
from os import remove
import random

QUOTES = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "1,2,3 Boom. Your Sticker Has Betrayed You.",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pacc looks cool",
    "Taking This Sticker Under My Remand...",
    "That's A Lit Sticker Which You Don't Deserve,So NVM I'll Take It... ",
]

@register(outgoing=True, pattern="^.quotes") 
        
      async def quotes(txt):          
         txt.edit(f"{random.choice(QUOTES)}")

CMD_HELP.update({
    "quotes":
    ".quotes\
\nUsage: Replies With A Random Quote.\
