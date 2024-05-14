#!/usr/bin/env python3

from babel.dates import format_time, format_date
from pytz import timezone
from datetime import datetime


d = datetime.utcnow()
print(format_date(d, locale='en'))
print(format_time(d, locale='en'))
