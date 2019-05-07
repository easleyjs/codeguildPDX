from django.conf import settings
from django.db import models
from django.utils import timezone
from math import floor
import string
"""
Int to Base 62 function from:
https://impythonist.wordpress.com/2015/10/31/building-your-own-url-shortening-service-with-python-and-flask/
"""


def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res


# Create your models here.
class URL(models.Model):
    long_url = models.CharField(max_length=500, blank=True)
    short_url = models.CharField(max_length=200, blank=True)

    def shorten_url(self, pk):
        self.short_url = toBase62(pk)

    def __str__(self):
        return self.short_url
