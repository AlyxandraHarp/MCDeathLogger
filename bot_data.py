##############################################
# DESCRIPTION:
# Important variables for logic
##############################################

# Reads every line in text file that user has already written to manually
def read_file():
    # SAMPLE TEXT IN KEY.TXT:
    # <channel ID>           -- get this at the end of a discord server channel url
    # <bot token>            -- get this on discord developer site
    # <path of server log>   -- get this by checking your mc server files, the log file may be called 'latest.log'
    with open("key.txt", "r") as text_file:
        data = text_file.readlines()
    return data

# Grab first line of text file
CHANNEL =  int((read_file()[0]).strip()) # Strip string just in case code reads '\n' at the end of the line
# Grab second line of text file
TOKEN = read_file()[1].strip() 
# Grab third line of text file
LOGPATH = read_file()[2].strip() 

# List of all common (Vanilla) death messages
# Duplicates removed, and p1, p2, p3 removed as a lot of the messages have these phrases in common
# Full list of death messages can be found in the en_us.json file in jar file
DEATH_MESSAGES = ["fell"
,"was doomed to fall"
,"was struck"
,"went up in flames"
,"walked into fire"
,"burned to death"
,"was burnt to a crisp"
,"tried to swim in lava"
,"discovered the floor was lava"
,"walked into danger zone"
,"suffocated in a wall"
,"was squished"
,"drowned"
,"died from dehydration"
,"starved to death"
,"was pricked to death"
,"walked into a cactus"
,"died"
,"blew up"
,"was blown up"
,"was killed"
,"withered away"
,"was shot"
,"was squashed"
,"was skewered"
,"was obliterated"
,"was slain"
,"was fireballed"
,"was pummeled"
,"was impaled"
,"hit the ground too hard"
,"fell out of the world"
,"didn't want to live in the same world as"
,"was roasted in dragon breath"
,"experienced kinetic energy"
,"went off with a bang"
,"was poked to death"
,"was stung to death"
,"froze to death"]

# List of possible user commands that will trigger the bot
USER_CMD = ["!start", "!help"] 