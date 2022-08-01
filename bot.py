import discord
import logging

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTAwMzY5NDY4MzI4Njk0NTkyMw.GvkF8r.rthevLKRQzyY3IElWQJE_pdALklBAw6xDhtHYI')