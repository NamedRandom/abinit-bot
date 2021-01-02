import discord
import re
import time
import multiprocessing
import os
import subprocess
from discord.ext import commands
import random

obj = type('', (), {})()
obj.url = "test"
obj.cloudOn = False
bot = commands.Bot(command_prefix='?')
bot.remove_command("help")
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def spam(ctx,arg):
    for x in arg:
        await ctx.send(arg)

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
    output = os.popen("timeout 30 /snap/bin/gcloud compute instances stop instance --zone=us-east4-b").read()
    print(output)
    await ctx.send("Stopped Cloud")
    obj.cloudOn = False

@bot.command(pass_context=True)
async def stop(ctx):
    await ctx.send("killing abinit...")
    print(os.popen("timeout 15 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command=\"sudo killall abinit\"").read())
    await ctx.send("killed.")

@bot.command(pass_context=True)
async def startCloud(ctx):
    await ctx.send("Starting Cloud")
    output = os.popen("timeout 30 /snap/bin/gcloud compute instances start instance --zone=us-east4-b").read()
    print(output)
    cmd = "\"tmux new-session -d /home/asphyxia/bot.sh\""
    print("sleeping 20")
    time.sleep(20)
    print("*yawn*")
    print(os.popen("timeout 10 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command="+cmd).read())
    await ctx.send("Started Cloud")
    cmd = "\"sudo shutdown 5\""
    print(os.popen("timeout 10 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command="+cmd).read())
    obj.cloudOn = True

@bot.command(pass_context=True)
async def startCloudBot(ctx):
    cmd = "\"/home/asphyxia/bot.sh\""
    print(os.popen("timeout 10 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command="+cmd).read())
    await ctx.send("i hope it worked")

@bot.command(pass_context=True)
async def checkBot(ctx):
        cmd = "\"ps -A | grep python3\""
        output = os.popen("timeout 30 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command="+cmd).read() 
        if output !="":
            print(output)
            await ctx.send(output)


@bot.command(pass_context=True)
async def checkAbinit(ctx):
        cmd = "\"ps -A | grep abinit\""
        output = os.popen("timeout 30 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command="+cmd).read() 
        print(output)
        await ctx.send(output)

@bot.command(pass_context=True)
async def kill(ctx,pid):
        cmd = "\"sudo kill "+pid+"\""
        output = os.popen("timeout 30 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b kinstance --command="+cmd).read() 
        ctx.send("Killed")


@bot.command(pass_context=True)
async def iterations(ctx):
        output = "No current abinit"
        cmd = "\"/home/asphyxia/abinit-bot/folderName.sh "+obj.url+"\""
        folder = os.popen("timeout 30 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command="+cmd).read() 
        await ctx.send("found folder as:"+folder)
        cmd = "\"cat /home/asphyxia/abinit-bot/downloads/"+re.sub('[^A-Za-z0-9]+', '', folder)+"/tbase*_*.out | grep Iteration\""
        output = os.popen("timeout 30 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command="+cmd).read() 
        print(output)
        await ctx.send(output)
        return output

@bot.command(pass_context=True)
async def status(ctx):
    onOff = os.popen("gcloud compute instances list | tail -n 1").read()
    await ctx.send(onOff)

@bot.command(pass_context=True)
async def clearFolder(ctx):
    cmd = "\"sudo rm -rf /home/asphyxia/abinit-bot/downloads\""
    print(os.popen("timeout 15 gcloud beta compute --project master-engine-246415 ssh --zone us-east4-b instance --command="+cmd).read())
    await ctx.send("**y e e t**")
        

@bot.command(pass_context=True)
async def cloudRun(ctx,arg):
        obj.url = arg


@bot.command(pass_context=True)
async def help(ctx):
    await ctx.send("?abinit to run non-cloud calc\n\nCloud Stuff:\n\tYou **MUST** start cloud calculations before local ones!!!\n\t?startCloud to start\n\t?stopCloud to kill cloud\n\t?cloudRun <link> to run cloud calculation")

bot.run('token') 
