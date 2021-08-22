import time
import random
from discord.ext import commands

fuckyou = commands.Bot(command_prefix="l", self_bot=True)
key = "NzM4NjA5NjY2NTA1ODM0NTE3.YNWyuA.o8ooSIW1TfLwCuANrw-_hLMJtIY"


@fuckyou.event
async def on_ready():
    print("Let's go")


@fuckyou.command()
async def se(ctx):
    while True:
        await ctx.send("pls beg")
        time.sleep(8)
        await ctx.send("pls deposit max")
        time.sleep(7)
        await ctx.send("pls give all @AlexTheIdiot#1782")
        time.sleep(4)
        await ctx.send("pls hunt")
        time.sleep(9)
        await ctx.send("pls fish")
        time.sleep(8)
        await ctx.send("pls dig")
        time.sleep(8)


fuckyou.run(key, bot=False)