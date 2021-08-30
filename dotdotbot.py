# bot.py
import os
import subprocess
import discord
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = 'TOKEN HERE'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    if message.author.bot:
        return
    
    if message.content[:6] == "+print":
        tempy = message.content[6:]
        if tempy[0] == ' ':
            tempy = tempy[1:]
        tempy = message.author.nick + ' said: ' + tempy 
        requests.post("http://127.0.0.1:5000/print", json={"content": tempy})
        await message.channel.send("printing...")

client.run(TOKEN)
