import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "24/7 Online ┊ 6AM - 10PM Online ┊ fast Respond ┊ Happy New Year 2022.", url = "https://www.twitch.tv/become_capsl"))


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
