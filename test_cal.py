from calendar_api.calendar_api import google_calendar_api
import datetime

now = datetime.datetime.now()# Get current time
duration = 7 # The duration of the training process
delta = datetime.timedelta(days=duration) # A duration expressing the difference between two date, time, or datetime instances to microsecond resolution. 

print (now.strftime('%Y-%m-%d %H:%M:%S'))

n_days = now + delta
print (n_days.strftime('%Y-%m-%d %H:%M:%S'))

year = str(now.year)
month = str(now.month).zfill(2)
day = str(now.day).zfill(2)
hour = str(now.hour-8).zfill(2)#　To adjust UTC+8 to UTC
minute = str(now.minute).zfill(2)
second = str(now.second).zfill(2)

month_end = str(n_days.month).zfill(2)
day_end = str(n_days.day).zfill(2)

start = year + '-' + month + '-' + day + 'T' + hour + ':' + minute + ':' + second + 'Z'
end = year + '-' + month_end + '-' + day_end + 'T' + hour + ':' + minute + ':' + second + 'Z'

print (start)
print (end)

m=google_calendar_api()
m.create_event(calendar_id='<your calendar id>',
start=start,
end=end,
desc='foo'
)
