import os
from disnake import Intents
from disnake.ext import commands
from decouple import config


token = config("TOKEN")
prefix = "?"
    
bot = commands.Bot(command_prefix=prefix, intents=Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot has been started!")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:3]}")

bot.run(token)