import asyncio
import discord
import os

client = discord.Client

@client.event
async def on_message(message)
    if message.author.bot:
        return
    if message.content == ""
        channel= client.get_channel()
        message = ""
        return await channel.send(message)


client.run(os.environ['TOKEN'])