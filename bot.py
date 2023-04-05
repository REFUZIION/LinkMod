import asyncio
import os
import re

import disnake
from disnake.ext import commands

with open('.env') as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value

BOT_TOKEN = os.environ['TOKEN']
CHANNEL_ID = 622096446237179924
ALLOWED_KEYWORDS = [".mp4", ".gif", ".png", ".jpg", ".jpeg", "mp4", "gif", "png", "jpg", "jpeg"]

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID:
        return

    if message.author == bot.user:
        return

    url_match = re.search("(?P<url>https?://[^\s]+)", message.content)
    if url_match:
        url = url_match.group("url")

        if any(keyword in url for keyword in ALLOWED_KEYWORDS):
            pass
        else:
            await message.delete()

            bot_message = await message.channel.send(
                f"{message.author.mention} Links are not allowed, except for gifs and images.")
            await asyncio.sleep(5)
            await bot_message.delete()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


bot.run(BOT_TOKEN)
