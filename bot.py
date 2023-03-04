import discord
import responses
import bot_data
import time
import os
from typing import Iterator
import typing # For typehinting 
import functools
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
channel = bot_data.CHANNEL

"""class AsyncWrite(threading.Thread):
#send log message when a player dies
    def __init__(self, sleep_sec=0.1):
        with open("log.txt", 'r') as file:
            threading.Thread.__init__(self)
            self.file = file
            self.sleep_sec = sleep_sec"""

def follow(file, sleep_sec=0.5) -> Iterator[str]:
    '''generator function that yields new lines in a file'''
    # seek the end of the file
    file.seek(0, os.SEEK_END)
    while True:
        # read last line of file
        line = file.readline()
            # sleep if file hasn't been updated
        if not line:
            time.sleep(sleep_sec)
            continue
        yield line.strip()

async def run_blocking(blocking_func: typing.Callable, *args, **kwargs) -> typing.Any:
    """Runs a blocking function in a non-blocking way"""
    func = functools.partial(blocking_func, *args, **kwargs) # `run_in_executor` doesn't support kwargs, `functools.partial` does
    return await client.loop.run_in_executor(None, func)

#send message to channel from player prompt
async def send_message(message, user_message):
    try:
        if user_message in bot_data.USER_CMD:
            response = responses.handle_response(user_message)
            await message.channel.send(response)
            #############################
            # Start logging
            #############################
            if (user_message == '!start'):
                with open(bot_data.LOGPATH, 'r') as file:
                    r = await run_blocking(follow, file, sleep_sec=0.1)
                    for line in r:
                        for d in bot_data.DEATH_MESSAGES:
                            if d in line and "[Server thread/INFO]" in line and "Named Entity" not in line:
                                print(f'> {line}')
                                await message.channel.send(f'> {line}')

    except Exception as e:
        print(e)

def run_discord_bot():
    global client
    global channel 
    #print to show bot is alive
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    #send message when user calls for bot
    @client.event
    async def on_message(message):
        if message.channel.id == channel:
            if message.author == client.user:
                return 
            user_message = str(message.content)
            await send_message(message, user_message)
    
    # Runs Deathlogger
    client.run(bot_data.TOKEN)
   

        
