import os
import asyncio
from discord.ext import commands
import discord
from keep_alive import keep_alive

key = os.environ['token']
fuckyou = commands.Bot(command_prefix="l", self_bot=True)


@fuckyou.event
async def on_ready():
    print("Let's go")


@fuckyou.command()
async def se(ctx):
    while True:
        await ctx.send("pls beg")
        await asyncio.sleep(8)
        await ctx.send("pls deposit max")
        await asyncio.sleep(11)
        await ctx.send("pls hunt")
        await asyncio.sleep(9)
        await ctx.send("pls fish")
        await asyncio.sleep(8)
        await ctx.send("pls dig")
        await asyncio.sleep(8)

@fuckyou.command()
async def stop(ctx):
  exit()

keep_alive()
fuckyou.run(key, bot=False)
