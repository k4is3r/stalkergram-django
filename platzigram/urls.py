""" """
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('hello-world/', hello_world)
]
#    path('admin/', admin.site.urls),
