####################################################################################################
# DESCRIPTION:
# Start up bot, ready user commands in specified channel, read live log data for most recent death
####################################################################################################

import discord
import responses
import bot_data
import time
import os
from typing import Iterator
import typing # For typehinting 
import functools
import asyncio
import aiofiles

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
channel = bot_data.CHANNEL

# Generator function that yields new lines in a file
async def follow(message) -> Iterator[str]:
    # seek the end of the file
    async with aiofiles.open(bot_data.LOGPATH, mode='r') as file:
        await file.seek(0, os.SEEK_END)
        while True:
            # read last line of file
            line = await file.readline()
            # sleep if file hasn't been updated, sleep
            if not line:
                continue
            else:
                if ("[Server thread/INFO]" in line) and (any((match := substring) in line for substring in bot_data.DEATH_MESSAGES)): #add <and "Named entity" not in line> to only have player deaths
                    #this prints messages once when at least one death message is found in list
                    print("HERE!")
                    print(f'Keyword: {match} on Line :{line.strip()}')
                    yield line.strip()
                

# Runs the blocking-heavy function is a non-blocking way
# Reason for implimentation: Discord.gateway warning "Shard ID None heartbeat blocked for more than 10 seconds."
async def run_blocking(blocking_func: typing.Callable, *args, **kwargs) -> typing.Any:
    func = functools.partial(blocking_func, *args, **kwargs) # `run_in_executor` doesn't support kwargs, `functools.partial` does
    return await client.loop.run_in_executor(None, func)

# Read and follow log for death messages
async def log_handler(message):
    
        print("before await")
        #f = await asyncio.create_task(run_blocking(follow, file, message))
        task = await run_blocking(follow, message)
        #a = await loop.run_until_complete(task)
        print("after await")
        async for line in task:
            print(line)
            await message.channel.send(f'> {line}')
        # Check if new line contains text for a death message
            

# Send message to channel from player prompt
async def send_message(message, user_message):
    # Check if user message is a valid command, else do nothing
    if user_message in bot_data.USER_CMD:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
        # Start reading log if user command calls start 
        if (user_message == '!start'):
            await log_handler(message)
                    
# Called from main, send message when bot is ready, and send messages when users send commands
def run_discord_bot():
    global client
    global channel 
    try:
        # Show bot is alive in system output
        @client.event
        async def on_ready():
            print(f'{client.user} is now running!')

        # Send message when user calls a bot command
        @client.event
        async def on_message(message):
            # Check if message is in specified channel, if not, do nothing 
            if message.channel.id == channel:
                if message.author == client.user:
                    return 
                user_message = str(message.content)
                # Determine bot action based on user message
                await send_message(message, user_message)
        
        # Runs Deathlogger
        client.run(bot_data.TOKEN)
    except Exception as e:
        print(e)

        
