import discord
import os
from discord.ext import commands
from discord import app_commands
from config import token

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ">", case_insensitive = True, intents=intents)

async def carregar_cogs():
  for arquivo in os.listdir('Cogscommands'):
    if arquivo.endswith('.py'):
      await client.load_extension(f"Cogscommands.{arquivo[:-3]}")
  for arquivo in os.listdir('Cogsevents'):
    if arquivo.endswith('.py'):
      await client.load_extension(f"Cogsevents.{arquivo[:-3]}")

@client.event
async def on_ready():
  await carregar_cogs()
  await client.tree.sync()
  print('Entramos como {0.user}' .format(client))
  

client.run(token)