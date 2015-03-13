# statistics data per month  dynamicly, you need get monthes behind a satrt time.

from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY


def get_tm():
    begin = datetime(2013, 5, 1)
    one_month = relativedelta(months=+1)
    end = datetime.now()
    months = [(d.year, d.month) for d in rrule(MONTHLY, dtstart=begin, until=end)]
    for m in months:
        print  datetime(m[0], m[1], 1)
        print  datetime(m[0], m[1], 1) + one_month
