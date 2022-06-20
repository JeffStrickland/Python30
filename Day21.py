"""
Day 21 - Datetime

Convert the following string dates to datetime format:
December 1th, 2015 15:30
5 June 2018 5pm
2020/9/13 00:05:06
"""
from datetime import datetime
from datetime import timedelta
from datetime import date

date1 = datetime(2015, 12, 1, 15, 30)
# ---> 2015-12-01 15:30:00
date2 = datetime(2018, 6, 5, 17)
# ---> 2018-06-05 17:00:00
date3 = datetime(2020, 9, 13, 5, 6)
# ---> 2020-09-13 05:06:00

"""
Using the operations between dates, find out what is the difference
in days, months and years from January 1, 2000 to today
"""

x = date.today()
y = date(2000, 1, 1)
z = x - y
print(z)
# ---> 8206 days, 0:00:00

## Should have checked more thoroughly before begining.  The author of this 30 day Python
## challenge didn't complete the past day 21.
