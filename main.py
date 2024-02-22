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

@client.event
async def on_ready():
  await carregar_cogs()
  await client.tree.sync()
  print('Entramos como {0.user}' .format(client))

@client.event
async def on_member_join(member):
  bemvindo = client.get_channel(1206188196250124301)
  geral = client.get_channel(1206334498749554738)

  embed = discord.Embed(
    title = 'Boas-Vindas',
    description = f'Seja bem vindo {member.mention}, esse é um servidor de teste e conver no {geral.mention}',
    colour = 11598249
  )

  embed.set_author(name='Dino',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiL_lZLfiyji8RFQVaJIaiRYAm9wd-HVXyyg&usqp=CAU')
  embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqNqi2PUXY2BooK-H7VZxL8Sx8EvifPX_4HR1yqtw81ZmpDGo1rt8MklEbDRV8UowiSDQ&usqp=CAU')
  embed.set_image(url= f'{member.avatar}')

  mensagem = await bemvindo.send(f"{member.mention}", embed= embed)
  

client.run(token)