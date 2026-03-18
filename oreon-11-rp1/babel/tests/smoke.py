from datetime import date
from babel.dates import format_date

assert format_date(date(2021,3,1), locale='en') == 'Mar 1, 2021'
