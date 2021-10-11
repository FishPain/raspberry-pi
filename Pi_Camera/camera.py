"""
Date: 2021-11-10
Author: Tony Yu Haotong

Program Description: 
    This program is used to take photos every [n] interval.
    It intergrates an external media device with a RaspberryPi.
    The photos are saved in the current directory.

Copyright (c) 2021, Fishpain
All rights reserved.

"""

import os
import time
from datetime import datetime
import json


# Load the configuration file
with open('Pi_Camera\config.json') as config_file:
    config = json.load(config_file)
    try:
        FRAME = config["frame"]         # frame rate
        assert FRAME > 0 and isinstance(FRAME, int), "Frame rate must be a positive integer"

        INTERVAL = config["interval"]   # Take photos every x seconds
        assert FRAME > 0 and isinstance(INTERVAL, int), "Interval must be a positive integer"

        MAX_TIME = config["max_time"]   # Number of hours it need to run
        assert FRAME > 0 and isinstance(MAX_TIME, int), "Max time must be a positive integer"

    except KeyError:
        print("Error: Please check the configuration file")
        exit()



def take_photo(FRAME, date_time):
    command = 'fswebcam -F ' + str(FRAME) + ' -r 1280x720 --no-banner ' + str(date_time) +'.jpg'
    os.system(command)

# a function that runs take_photo() every one hour
def take_photos(INTERVAL, MAX_TIME):
    count = 0
    while count < MAX_TIME:
        now = datetime.now()
        take_photo(FRAME, now.strftime("%Y-%m-%d_%H-%M-%S"))
        time.sleep(INTERVAL)
        count += 1

take_photos(INTERVAL, MAX_TIME)