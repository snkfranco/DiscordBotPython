import discord
from discord.ext import commands

from apikey import *

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot já está em execução')

@client.command()
async def ola(ctx):
    await ctx.send('Olá, tudo bem? Eu sou o bot do Youtube!')

@client.command()
async def tchau(ctx):
    await ctx.send('Até mais, te vejo em breve!')

client.run(bot_token)