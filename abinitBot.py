import discord
import os
import subprocess
from discord.ext import commands
import random


bot = commands.Bot(command_prefix='?')

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
    output = os.popen("/snap/bin/gcloud compute instances stop kelvin-is-gay --zone=us-east4-b").read()
    print(output)
    await ctx.send("Stopped Cloud")
@bot.command(pass_context=True)
async def startCloud(ctx):
    output = os.popen("/snap/bin/gcloud compute instances start kelvin-is-gay --zone=us-east4-b").read()
    print(output)
    cmd = "\"nohup bash /home/asphyxia/bot.sh &\""
    print(os.popen("gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b kelvin-is-gay --command="+cmd).read())
    await ctx.send("Started Cloud")

@bot.command(pass_context=True)
async def cloudRun(ctx,arg):
    await ctx.send("running on cloud...")
    output = subprocess.check_output(["./abinitMulti.sh",arg]).decode()
    print(output)
    await ctx.send(output+"\n <@259472979031883776>")
    stopCloud()

bot.run('NTk1MDQ5MzE2OTE4NDkzMTg1.XRlU4A.s8QJDYk9AuD4rMCeXS8AIsB457M') 
