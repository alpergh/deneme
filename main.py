import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def mem(ctx):

    sayi=random.choice(["0","1","2","3","4","5","6","7","8","9"])

    if sayi in "123456":
        with open('images/mem1.png','rb') as f:
            picture = discord.File(f)

    elif sayi in "789":
        with open('images/mem2.jpg','rb') as f:
            picture = discord.File(f)

    elif sayi == "0" :
        with open('images/mem3.jpg','rb') as f:
            picture = discord.File(f)

bot.run("")
