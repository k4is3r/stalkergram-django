from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('hello-world',)
]
#    path('admin/', admin.site.urls),

def hello_world(request):