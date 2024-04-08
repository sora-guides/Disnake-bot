import os
from disnake import Intents
from disnake.ext import commands
from decouple import config


TOKEN = config("TOKEN")
prefix = "?"
    
bot = commands.Bot(command_prefix=prefix, intents=Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready() -> None:
    print("Bot has been started!")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:3]}")
        # expect: cogs.mod

bot.run(TOKEN)

"""
Для запуска бота необходим токен, экземпляр бота и интенты.
Также немного раскидал по базовым командам и cogs -> аналог хэндлеров для этой библиотеки.
Сама же библиотека написана асинхронно.
"""