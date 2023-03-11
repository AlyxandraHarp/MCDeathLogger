#########################################
# DESCRIPTION:
# Send response messages to server 
#########################################

import bot_data

# convert user message to lowercase, determine bot response based on user message
def handle_response(message) -> str:
    p_message = message.lower()
    
    # Sends message to server that bot is now reading the logs
    if p_message == bot_data.USER_CMD[0]:
        response = 'Starting Death Tracker...'
        return response

    # Sends information on commands
    if p_message == bot_data.USER_CMD[1]:
        lstr = ['`!start = grabs death messages from the Minecraft server in real time`']
        delimiter = ' '
        final_str = delimiter.join(map(str, lstr))
        return final_str

