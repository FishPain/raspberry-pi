import os
import time
from datetime import datetime


FRAME = 16 # frame rate
INTERVAL = 30 # Take photos every x seconds
MAX_TIME = 3  # Number of hours it need to run


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