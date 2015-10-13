"""
>>> yury = Person()
>>> print yury.name
None
>>> yury.name = "Yury Krasouski"
>>> print yury.name
Yury Krasouski
>>> yury.birthday = datetime.strptime("1986-04-09", "%Y-%m-%d")
>>> yury.phone = "375 25 9355570"
>>> print yury.phone
375 (25) 935-55-70
>>> print yury.birthday
1986-04-09 00:00:00
>>> yury.birthday = "April 09"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Birthday must be datetime type
>>> yury.name = None
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Name must be string type
>>> yury.phone = "375 (25) 9355570"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Phone must be in format XXX XX XXXXXXX
"""

import re
from datetime import datetime


class BirthdayField(object):
    def __init__(self):
        self._birthday = None

    def __get__(self, instance, owner):
        return self._birthday.strftime("%Y-%m-%d %H:%M:%S")

    def __set__(self, instance, value):
        if isinstance(value, datetime):
            self._birthday = value
        else:
            raise TypeError('Birthday must be datetime type')


class NameField(object):
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value):
        if isinstance(value, str):
            self._name = value.title()
        else:
            raise TypeError('Name must be string type')


class PhoneField(object):
    def __init__(self):
        self._phone = None
        self._re_phone = re.compile(r'(\d{3}) (\d{2}) (\d{7})')

    def __get__(self, instance, owner):
        return self._phone

    def __set__(self, instance, value):
        match_result = self._re_phone.match(value)
        if match_result:
            t = match_result.groups()
            self._phone = ''.join([
                str(t[0]), ' (', str(t[1]), ') ', str(t[2][:3]), '-', str(t[2][3:5]), '-', str(t[2][5:])])
        else:
            raise ValueError('Phone must be in format XXX XX XXXXXXX')


class Person(object):
    name = NameField()
    birthday = BirthdayField()
    phone = PhoneField()
