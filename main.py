import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # This grabs the channelID from the env variable

BUMP_INTERVAL = 40

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('Bot is ready to bump!')
    auto_bump.start()

@tasks.loop(seconds=BUMP_INTERVAL)
async def auto_bump():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("/JakeKunitserNeedstoChangeHisDiaper")
        print(f"Bump sent in {channel.name}")

@bot.command()
async def ping(ctx):
    await ctx.send("Bot is running! Auto-bump is active.")

bot.run(os.getenv('DISCORD_TOKEN'))  # Get token from environment