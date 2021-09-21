import os
import time
from datetime import date


FRAME = 24


def take_photo(FRAME, date_time):
    command = 'fswebcam -F ' + str(FRAME) + '-r 1280x720 --no-banner ' + str(date_time) +'.jpg'
    os.system(command)

# a function that runs take_photo() every one hour
def take_photos():
    while True:
        take_photo(FRAME, date.today())
        time.sleep(60)

take_photos()