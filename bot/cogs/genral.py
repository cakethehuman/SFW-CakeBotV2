import logging

import discord
from discord import app_commands
from discord.ext import commands

from ..services.apiService import getResultData

logger = logging.getLogger(__name__)


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="backagain", description="Baby im back")
    async def im_back_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Yoo cake is back",
            description="IS aliveeee"
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="server", description="Get Server player info")
    async def im_back_command(self, interaction: discord.Interaction):
        data = getResultData()
        embed = discord.Embed(
            title = "Player count ig",
            description=f"""Eagle's Vanilla I Scream player count : {data[0]}\n
                            Eagle's Vanilla U Scream player count : {data[1]}\n
                            Eagle's Yummy Dreamst : {data[2]}\n""",
            color=discord.Color.blue()
        )
        await interaction.response.send_message(embed=embed)
    
    
async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))