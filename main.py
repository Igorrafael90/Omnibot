import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ">", case_insensitive = True, intents=intents)

@client.event
async def on_ready():
  await client.tree.sync()
  print('Entramos como {0.user}' .format(client))

@client.tree.command(description='repetir mensagem do usuario')
async def falar(interact:discord.Interaction,frase:str):
  await interact.response.send_message(frase) 

@client.command()
async def kick(ctx, member: discord.Member, *, reason: str = None):
  if reason == None:
    reason = "Sem nenhum por motivo por" + ctx.message.author.name
  if member == ctx.author:
    return await ctx.send("Você nao pode banir a si mesmo")
  if member == client.user:
    return await ctx.send("Você nao pode me banir")
  
  if ctx.author.guild_permissions.ban_members:
    embed = discord.Embed(
      title='Expulso',
      description=f'O membro {member.name}, foi banido por {reason}',
      color= 11598249
    )
    embed.set_author(name=f'{member.name}',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiL_lZLfiyji8RFQVaJIaiRYAm9wd-HVXyyg&usqp=CAU')
    embed.set_thumbnail(url=f'{member.avatar}')

    await member.kick(reason=reason)
    await ctx.send(f'Relatorio', embed = embed)
  else:
    await ctx.send('Você não tem permissao para expulsar')
    
@client.command()
async def perfil(ctx, member:discord.Member):
  embed = discord.Embed(
    title='Perfil',
    description=f'Aqui está o perfil de {member.mention}',
    color= 11598249
  )
  embed.set_author(name=f'{member.name}',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiL_lZLfiyji8RFQVaJIaiRYAm9wd-HVXyyg&usqp=CAU')
  embed.set_thumbnail(url=f'{member.avatar}')
  
  embed.add_field(name='Nome',value=f'{member.display_name}')
  embed.add_field(name='Data',value=f'{member.created_at}')
  embed.add_field(name='id', value=f'{member.id}', inline=False)

  await ctx.send("aqui esta o perfil", embed=embed)

@client.command()
async def apagar(ctx,amount: int = None):
    if ctx.author.guild_permissions.ban_members:
      await ctx.channel.purge(limit= amount)
      embed = discord.Embed(
        title='Limpeza',
        description=f'As {amount} mensagens foram apagadas',
        color= 11598249
      )
      embed.set_author(name=f'{ctx.author.name}',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiL_lZLfiyji8RFQVaJIaiRYAm9wd-HVXyyg&usqp=CAU')
      await ctx.send(embed=embed, delete_after = 3)
    else:
      await ctx.send('Você não tem permissao para apagar as mensagens')

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
  

client.run('token')