""" """
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello coders!')


urlpatterns = [
    path('hello-world/', hello_world)
]
#    path('admin/', admin.site.urls),
