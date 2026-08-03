import logging

import discord
from discord import app_commands
from discord.ext import commands
from strip_tags import strip_tags

from ..core.server_update import servers_cache

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
    async def server_command(self, interaction: discord.Interaction):
        descriptionText = ""
        embed = discord.Embed(
            description=descriptionText,
            url="https://static2.klipy.com/ii/a8ada81afc59159ea5c8927feffa2e31/fe/3e/km0AUNJRv5AxqtIkWos.gif",
            type="gifv"
        )
        for server in servers_cache:
            embed.description = str(embed.description) + f"\n"
        await interaction.response.send_message(ephemeral=True, embed=embed)
        # await interaction.response.send_message(ephemeral=True, content="https://static2.klipy.com/ii/a8ada81afc59159ea5c8927feffa2e31/fe/3e/km0AUNJRv5AxqtIkWos.gif")
    
async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))