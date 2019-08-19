""" Platzigram views"""
# Django
from django.http import HttpResponse
# Utilities
from datetime import datetime
import json


def hello_world(request):
    now = str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))
    return HttpResponse('Hello coders! current time server is {}'.format(now))


def sorted_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {} you are not allowed here'.format(name)
    else:
        message = 'Welcome {}, to platzigram'.format(name)

    return HttpResponse(message)
