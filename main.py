import discord
from discord.ext import commands, tasks
import asyncio

# Bot setup with all intents enabled
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Replace these with your values
CHANNEL_ID = 123456789  # The channel ID where you want to send bumps
BUMP_INTERVAL = 7200    # 2 hours

@bot.event
async def on_ready():
    print(f'Bot is logged in as {bot.user}')
    auto_bump.start()
    
@tasks.loop(seconds=BUMP_INTERVAL)
async def auto_bump():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("/bump")
        print(f"Bump sent in {channel.name}")

# Add  ping command to see if bot is running 
@bot.command()
async def status(ctx):
    await ctx.send("Bot is running! Auto-bump is active.")

# Run the bot
bot.run('YOUR_BOT_TOKEN')