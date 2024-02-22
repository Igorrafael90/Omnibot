import discord
from discord.ext import commands
from discord import app_commands

class Apagar(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()
        
    @app_commands.command(name='apagar',description='apague a quantidade de mensagens que quiser')
    async def apagar(self,interact: discord.Interaction,amount: int = None):
        if interact.user.guild_permissions.ban_members:
            await interact.channel.purge(limit= amount)
            embed = discord.Embed(
            title='Limpeza',
            description=f'As {amount} mensagens foram apagadas',
            color= 11598249
            )
            embed.set_author(name=f'{interact.user.name}',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiL_lZLfiyji8RFQVaJIaiRYAm9wd-HVXyyg&usqp=CAU')
            await interact.response.send_message(embed=embed, delete_after = 3)
        else:
            await interact.response.send_message('Você não tem permissao para apagar as mensagens')
    

async def setup(client):
    await client.add_cog(Apagar(client))