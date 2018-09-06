# Write a function named minutes that takes two datetimes and, using
# timedelta.total_seconds() to get the number of seconds, returns the number of
# minutes, rounded, between them. The first will always be older and the second
# newer. You'll need to subtract the first from the second.
import datetime

def minutes(now, then):
    period = then - now
    output = round(period.total_seconds() / 60)
    return output


now = datetime.datetime.now()
then = datetime.datetime.now()


print(minutes(now, then))
