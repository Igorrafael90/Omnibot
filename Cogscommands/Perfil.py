import discord
from discord.ext import commands
from discord import app_commands

class Perfil(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()
        
    @app_commands.command(name='perfil', description='Veja as informaçoes de algum perfil')
    async def perfil(self,interact: discord.Interaction, member:discord.Member):
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

        await interact.response.send_message("aqui esta o perfil", embed=embed)

async def setup(client):
    await client.add_cog(Perfil(client))