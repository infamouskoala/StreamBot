import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
import time

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

TOKEN = input("enter token: ")
status = input("Status message: ")

@client.event
async def on_ready():
    os.system('clear')
    await client.change_presence(activity=discord.Streaming(name=status, url="https://twitch.tv/koala_from_mars"))
    print(f'Logged in as {client.user} ({client.user.id})')

keep_alive()
client.run(TOKEN, bot=False)
