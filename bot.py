import re, discord, asyncio

BOT_TOKEN = "Bot Token"
CHANNEL_ID = "Channel Id"
ALLOWED_KEYWORDS = [".mp4", ".gif", ".png", ".jpg", ".jpeg", "mp4", "gif", "png", "jpg", "jpeg"]

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID:
        return

    if message.author == client.user:
        return

    url_match = re.search("(?P<url>https?://[^\s]+)", message.content)
    if url_match:
        url = url_match.group("url")

        if any(keyword in url for keyword in ALLOWED_KEYWORDS):
            pass
        else:
            await message.delete()

            bot_message = await message.channel.send(f"{message.author.mention} Links are not allowed, except for gifs and images.")
            await asyncio.sleep(5)
            await bot_message.delete()

client.run(BOT_TOKEN)
