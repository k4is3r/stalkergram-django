""" Platzigram views"""
# Django
from django.http import HttpResponse
# Utilities
from datetime import datetime


def hello_world(request):
    now = str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))
    return HttpResponse('Hello coders! current time server is {}'.format(now))


def hi(request):
    return HttpResponse('Hi!')
