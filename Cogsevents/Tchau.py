import discord
from discord.ext import commands
from discord import app_commands

class Tchau(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        tchau = self.client.get_channel(1211134646482640908)
        
        embed =  discord.Embed(
            title='Tchau',
            description=f'Ja vai tarde {member.mention} e aprenda a deixar de ser boboca',
            colour = 11598249
        )
        embed.set_author(name='Dino',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiL_lZLfiyji8RFQVaJIaiRYAm9wd-HVXyyg&usqp=CAU')
        embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqNqi2PUXY2BooK-H7VZxL8Sx8EvifPX_4HR1yqtw81ZmpDGo1rt8MklEbDRV8UowiSDQ&usqp=CAU')
        embed.set_image(url= f'{member.avatar}')

        await tchau.send(f"{member.mention}", embed= embed)




async def setup(client):
    await client.add_cog(Tchau(client))
