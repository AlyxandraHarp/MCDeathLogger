import bot_data

"""def random_response():
    str_list = ["Huh? What do you want?", "What is it?", "Better watch it or you'll be next!", "*<skeleton noises>*"]
    return random.choice(str_list)"""

def handle_response(message) -> str:
    p_message = message.lower()

    #Sends list of all players that have joined the server
    """if p_message == '!players':
        players = "'<Player>'"
        return players

    #Sends list of all players and their death counts
    if p_message == '!deathtoll':
        death_cnt = "'<Player> : <Count>'"
        return death_cnt

    #get random messages from deathlogger himself
    if p_message == '!deathlogger':
        response = random_response()
        return response

    #PARAM: Player
    #Sends a player's list of all death messages
    if p_message == '!obituary':
        response = "'<Player> : <message>'"
        return response"""

    """if p_message == bot_data.USER_CMD[0]:
        response = f'Set DeathLogger to .'
        return response
    elif p_message == bot_data.USER_CMD[1]:
        response = f'Removing DeathLogger from .'
        return response"""
    
    if p_message == bot_data.USER_CMD[0]:
        response = 'Starting Death Tracker...'
        return response

    #Sends infomation on commands
    if p_message == bot_data.USER_CMD[1]:
        lstr = ['`!start = grabs death messages of server minecraft in real time`']
                #'`!player = list of all players who have joined the server`\n', 
                #'`!deathtoll = list of all players and their death counts`\n',
                #'`!deathlogger = get random messages from deathlogger himself`\n',
                #'`!obituary = list of a players list of all death messages`\n']
        delimiter = ' '
        final_str = delimiter.join(map(str, lstr))
        return final_str

