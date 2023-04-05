import disnake
from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot: commands.AutoShardedInteractionBot) -> None:
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Initialized /ping command.")

    @commands.slash_command(name="ping", description="Ping? Pong! find out my latency.")
    async def _ping(self, inter: disnake.CommandInteraction) -> None:
        await inter.response.defer()
        embed = disnake.Embed(
            description=f"🏓 Pong!\nMy latency is about **{int(self.__bot.latency * 1000)}ms**.",
            color=0xFF4D4D,
        )

        embed.set_footer(text=f"Developed by REFUZIION#1337 @ 2023")
        await inter.edit_original_message(embed=embed)


def setup(self: commands.AutoShardedBot) -> None:
    self.add_cog(Ping(self))
