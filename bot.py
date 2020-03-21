import discord
from discord.ext import commands
import asyncio
import datetime
from random import randint
import logging

daytime_names = ['The Park', 'The Forest', 'The Cafe', 'Building 16']
evening_names = ['The Hobbit', 'The Shooting Star', 'Stags']
night_names = ['The Edge', 'Jesters']

def SelectRandom(names):
    return names[randint(0, len(names))]

def GetName(current_name):
    now = datetime.datetime.now()
    if now.hour < 18 and now.hour > 5:
        if current_name in daytime_names:
            return current_name
        else:
            return SelectRandom(daytime_names)
    elif now.hour < 22:
        if current_name in evening_names:
            return current_name
        else:
            return SelectRandom(evening_names)
    else:
        if current_name in night_names:
            return current_name
        else:
            return SelectRandom(night_names)
    

async def update_meeting_place():
    while True:
        try:
            await asyncio.sleep(60) # update every minute
            channel = bot.get_channel(659792341581692960)
            await channel.edit(name=GetName(channel.name))
            print(f"Channel name is {channel.name}.")
        except Exception as e:
            print(f"Exception: {e}")



bot = commands.Bot(command_prefix = '!')

bot.loop.create_task(update_meeting_place())

# Log that the bot logs in successfully
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Only respond to dm messages which weren't from the bot
@bot.event
async def on_message(msg):
    if type(msg.channel) is discord.DMChannel and msg.author != bot.user:
        await bot.process_commands(msg)

tokenFile = open("token.txt", "r")
token = tokenFile.read().strip()

bot.run(token)