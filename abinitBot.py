import discord
import subprocess
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def abinit(ctx, arg):
    await ctx.send("running...")
    output = subprocess.check_output(["./abinit.sh",arg]).decode()
    print(output)
    await ctx.send(output)

@bot.command(pass_context=True)
async def ping(ctx):
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command(pass_context=True)
async def gay(ctx):
    await ctx.send("<@259472979031883776> is gay")

bot.run('NTk1MDQ5MzE2OTE4NDkzMTg1.XRlU4A.s8QJDYk9AuD4rMCeXS8AIsB457M') 
