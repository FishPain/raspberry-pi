import os
import time
from datetime import datetime


FRAME = 24
MAX_TIME = 3


def take_photo(FRAME, date_time):
    command = 'fswebcam -F ' + str(FRAME) + '-r 1280x720 --no-banner ' + str(date_time) +'.jpg'
    os.system(command)

# a function that runs take_photo() every one hour
def take_photos(MAX_TIME):
    count = 0
    while count < MAX_TIME:
        take_photo(FRAME, datetime.now())
        time.sleep(60)
        count += 1

take_photos(MAX_TIME)