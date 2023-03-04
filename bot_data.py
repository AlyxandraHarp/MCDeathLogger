def read_file():
    with open("key.txt", "r") as text_file:
        data = text_file.readlines()
    return data

CHANNEL =  int(read_file()[0]) #Channel ID is the second line of text file

TOKEN = read_file()[1] #Token is the first line of text file

LOGPATH = read_file()[2].strip()

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

USER_CMD = ["!start", "!help"] 
#Eventually may want: ["!players", "!deathtoll", "!deathcount", "!deathlogger", "!obituary", "!start", "!help"]
