'''
import time


print("Current Time: ", time.time())
print("Current Time: ", time.localtime(time.time()))
print("Current Time: ", time.asctime(time.localtime(time.time())))


import pytz

New_York = pytz.timezones('America/New York')
New_York_date_time = datetime.now(New_York)
print(New_York_date_time)

'''

import calendar

cal = calendar.month(2018,5)
print(cal)