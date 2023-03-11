import time


# Write to log file for testing, simulating a player's death
for i in range(0,60):
    logfile = open("latest.txt","a")
    logfile.write("17.11 17:18:09 [Server thread/INFO] Player was slain by zombie!\n") #logger should read this
    time.sleep(5)
    logfile.write("17.11 17:19:09 [Server thread/INFO] Player left the server.\n") #logger should ignore this
    time.sleep(1)
    logfile.close()
    
# Start and stop program as needed for testing
# Recommend leaving it on for a few seconds then stop it, 
#   then start again after 10 minutes to an hour to watch for blocked heartbeats in between runs
