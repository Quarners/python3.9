from datetime import datetime
from zoneinfo import ZoneInfo

"""
Use of zoneinfo module native to timezone
"""

current_time = datetime.now()
#print current time in my time zone
print(current_time)

current_time_angeles = datetime.now(ZoneInfo("America/Los_Angeles"))

#print  current time in any time zone
print(current_time_angeles)
