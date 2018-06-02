import calendar
from datetime import datetime

def add_gigasecond(birth_date):
    """
    Calculates date when the person will live 10^9 seconds.
    """

    # this line makes me appreciating JS implementation
    birth_timestamp = calendar.timegm(birth_date.timetuple())
    after_timestamp = birth_timestamp + 10 ** 9

    return datetime.utcfromtimestamp(after_timestamp)
