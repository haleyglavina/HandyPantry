#testing daily program run 
import schedule
import time
import datetime
from math import floor
import operator
import datetime
from threading import Timer
exec(open('foodItem_class.py').read())
exec(open('storing_fooditems.py').read())

def job():
    daily_check()
    return

schedule.every().day.at("13:19").do(job)

while True:
    schedule.run_pending()
    time.sleep(30) # wait one minute