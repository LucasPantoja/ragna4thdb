import discord
import os

from ragna4th import Ragna4th
from discord.ext import commands
from dotenv import load_dotenv
from io import StringIO

ragna4th_bot = Ragna4th()

load_dotenv()
token = os.environ.get('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def item(ctx, item_id):
    await ctx.channel.send(f'Procurando preços do Item')
    message = ragna4th_bot.show_item_prices(item_id)
    if message:
        if len(message) > 2000:
            buffer = StringIO(message)
            f = discord.File(buffer, filename="item.txt")
            await ctx.send(file=f)
        else:
            await ctx.send(f"``` {message} ```")
    else:
        await ctx.channel.send('Ops! Algo de errado aconteceu com a busca')


@bot.command()
async def relax(ctx):
    await ctx.channel.send(f'Procurando preços do Relaxamento...')
    miners = {
        'Etherium': '1000331',
        'Etherium Perfeito': '1000335',
        'Etherium Enriquecido': '1000333',
        'Etherdeocon': '1000332',
        'Etherdeocon Perfeito': '1000334',
        'Etherdeocon Enriquecido': '1000336',
        'Aquamarina Etérea': '1000325',
        'Topázio Etéreo': '1000326',
        'Ametista Etérea': '1000327',
        'Âmbar Etéreo': '1000328'
    }
    message = ''

    for item_name, item_id in miners.items():
        await ctx.send(f"Procurando {item_name}")
        message += ragna4th_bot.show_item_prices(item_id)
        if message:
            if len(message) > 2000:
                buffer = StringIO(message)
                f = discord.File(buffer, filename="relaxamento.txt")
                if item_id == list(miners.values())[-1]:
                    await ctx.send(file=f)


bot.run(token)
