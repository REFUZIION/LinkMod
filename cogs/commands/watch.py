import disnake
from disnake.ext import commands
from utils import readJsonData, writeJsonData


class Watch(commands.Cog):
    def __init__(self, bot: commands.AutoShardedInteractionBot) -> None:
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Initialized /watch command.")

    @commands.slash_command(name="watch", description="Watch this channel for links.")
    async def _watch(self, inter: disnake.CommandInteraction) -> None:
        await inter.response.defer()
        embed = disnake.Embed(color=0xFF4D4D)

        if inter.channel.permissions_for(inter.author).manage_channels:
            data = readJsonData("watched_channels.json")
            if str(inter.channel.id) not in data:
                data.append(str(inter.channel.id))
                writeJsonData("watched_channels.json", data)
                embed.description = f"Blocking links in this channel. This channel is being watched."
            else:
                embed.description = "This channel is already being watched for links."
        else:
            embed.description = "You do not have the permissions to execute this command!"

        embed.set_footer(text=f"Developed by REFUZIION#1337 @ 2023")
        await inter.edit_original_message(embed=embed)


def setup(self: commands.AutoShardedInteractionBot) -> None:
    self.add_cog(Watch(self))
