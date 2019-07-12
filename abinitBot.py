import discord
import os
import googleapiclient.discovery
import subprocess
from discord.ext import commands
import random

compute = googleapiclient.discovery.build('compute', 'v1')

proj='master-engine-246415'
zone='us-east4-b'
inst='kelvin-is-gay'


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
    await ctx.send(output+"\n <@259472979031883776>")

@bot.command(pass_context=True)
async def ping(ctx):
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command(pass_context=True)
async def gay(ctx):
    await ctx.send("<@259472979031883776> is gay")

@bot.command(pass_context=True)
async def stopCloud(ctx):
    output = compute.instances().stop(project=proj,zone=zone,resourceId=inst)
    print(output)
    await ctx.send(output)

@bot.command(pass_context=True)
async def startCloud(ctx):
    output = compute.instances().start(proj,zone,inst)
    print(output)
    await ctx.send(output)

@bot.command(pass_context=True)
async def cloudRun(ctx,arg):
    coreCount = subprocess.check_output(["grep -c ^processor /proc/cpuinfo",arg]).decode()
    if coreCount == 4:
        startCloud()
    else:
        await ctx.send("running on cloud...")
        output = subprocess.check_output(["./abinitMulti.sh",arg]).decode()
        print(output)
        await ctx.send(output+"\n <@259472979031883776>")
    stopCloud()
        

bot.run('NTk1MDQ5MzE2OTE4NDkzMTg1.XRlU4A.s8QJDYk9AuD4rMCeXS8AIsB457M') 
