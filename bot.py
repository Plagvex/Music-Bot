import discord
form discord.ext import commands
form discord.ext.commands import Bot
import asyncio
import random
import requests
import os

client = commands.Bot(command_prefix=".") 
player_dict = dict()


@client.event
async def on_ready():
    print("The Bot is now Online")


@client.command(pass_context=True)
async def play (ctx, url):
    channel = ctx.massage.author.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice = client.voice_client_in(server)
    player = await voice.create_ytdl_player(url)
    player_dict[server.id] = player
    await client.send_message(ctx.message.channel, "Playing `%s` now" % player.title)
    player.start()
    
    
@client.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    player.stop()
    await client.send_message(ctx.message.channel, "Stopped `%s`" % player.title)
    del player_dict[server.id]
    
    
@client.command(pass_context=True)
async def pause(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.pause()
    await client.send_message(ctx.message.channel, "Paused `%s`" % player.title)
    
    
@client.command(pass_context=True)
async def resume(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.resume()
    await client.send_message(ctx.message.channel, "Resumed `%s`" % player.title)




client.run(str(os.environ.get)('BOT_TOKEN')))
