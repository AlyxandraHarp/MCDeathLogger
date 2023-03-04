import time


# Write to log file for testing, simulating a player's death
for i in range(0,60):
    logfile = open("latest.log","a")
    logfile.write("17.11 17:18:09 [Server] [INFO] Player was slain by zombie!\n") #logger should read this
    time.sleep(5)
    logfile.write("17.11 17:19:09 [Server] [INFO] Player left the server.\n") #logger should ignore this
    time.sleep(1)
    logfile.close()
