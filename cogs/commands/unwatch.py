import disnake
from disnake.ext import commands

from utils import readJsonData, deleteJsonData


class Unwatch(commands.Cog):
    def __init__(self, bot: commands.AutoShardedInteractionBot) -> None:
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Initialized /unwatch command.")

    @commands.slash_command(name="unwatch", description="Stop watching this channel for links.")
    async def _unwatch(self, inter: disnake.CommandInteraction) -> None:
        await inter.response.defer()
        embed = disnake.Embed(color=0xFF4D4D)

        if inter.channel.permissions_for(inter.author).manage_channels:
            data = readJsonData("watched_channels.json")
            if str(inter.channel.id) in data:
                try:
                    deleteJsonData("watched_channels.json", str(inter.channel.id))
                    embed.description = f"Stopped blocking links in this channel. This channel is no longer being watched."
                except:
                    embed.title = 'Error: RFZ0000041'
                    embed.description = f"Something went wrong, you can report it to my developer @REFUZIION#1337 with the Error code."

            else:
                embed.description = "This channel is not being watched for links. You can change that by using `/watch`"
        else:
            embed.description = "You do not have the permissions to execute this command!"

        embed.set_footer(text=f"Developed by REFUZIION#1337 @ 2023")
        await inter.edit_original_message(embed=embed)


def setup(self: commands.AutoShardedInteractionBot) -> None:
    self.add_cog(Unwatch(self))
