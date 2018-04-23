from datetime import date, datetime, time, timedelta

def add_gigasecond(now):
    return now + timedelta(seconds=10**9)
dt = datetime.combine(date.today(), time())
print(add_gigasecond(dt))