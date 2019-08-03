from discord.ext import commands

client = commands.Bot(command_prefix=".") 
player_dict = dict()


@client.event
async def on_ready():
    print("The Bot is now Online")


@client.command(pass_context=True)
async def play (ctx, url):
    channel = ctx
