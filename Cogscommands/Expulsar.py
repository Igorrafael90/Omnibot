import discord
from discord.ext import commands
from discord import app_commands

class Expulsar(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()

    @app_commands.command(name='expulsar', description='expulsar membro')
    async def kick(self,interact: discord.Interaction, member: discord.Member, *, reason: str = None):
        if reason == None:
            reason = "Sem nenhum por motivo por" + interact.user.name
        if member == interact.user:
            return await interact.response.send_message("Você nao pode banir a si mesmo")
        if member == self.client.user:
            return await interact.response.send_message("Você nao pode me banir")
  
        if interact.user.guild_permissions.ban_members:
            embed = discord.Embed(
            title='Expulso',
            description=f'O membro {member.name}, foi banido por {reason}',
            color= 11598249
            )
            embed.set_author(name=f'{member.name}',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiL_lZLfiyji8RFQVaJIaiRYAm9wd-HVXyyg&usqp=CAU')
            embed.set_thumbnail(url=f'{member.avatar}')

            await member.kick(reason=reason)
            await interact.response.send_message(f'Relatorio', embed = embed)
        else:
            await interact.response.send_message('Você não tem permissao para expulsar')

async def setup(client):
    await client.add_cog(Expulsar(client))