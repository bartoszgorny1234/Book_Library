from django.db import models
from partial_date import PartialDateField
from partial_date import PartialDate
import datetime

date = PartialDate("2015")
print(date)
print(type(date.date))
print(date.date)
print(type(datetime.date(2012, 9, 21)))