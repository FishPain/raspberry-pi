import os
import time
from datetime import date


FRAME = 24


def take_photo(FRAME, date_time):
    os.system(f'fswebcam -F {FRAME} -r 1280x720 --no-banner image{date_time}.jpg')

# a function that runs take_photo() every one hour
def take_photos():
    while True:
        take_photo(FRAME, date.today().strftime('%Y%m%d%H%M%S'))
        time.sleep(60)