import os
from crontab import CronTab


FRAME = 24

#date-time = 0

#os.system(f'fswebcam -F {FRAME} -r 1280x720 --no-banner image{date-time}.jpg')


def main():
    with CronTab(user='root') as cron:
        job = cron.new(command=f'fswebcam -F {FRAME} -r 1280x720 --no-banner image21.jpg')
        job.minute.every(1)