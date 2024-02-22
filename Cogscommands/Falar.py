import discord
from discord.ext import commands
from discord import app_commands

class Falar(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()
        
    @app_commands.command()
    async def falar(self,interact:discord.Interaction,frase:str):
        await interact.response.send_message(frase)

async def setup(client):
    await client.add_cog(Falar(client))