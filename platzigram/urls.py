""" Platzi URL"""
from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('sorted/', views.sorted_int),
    path('hi/<str:name>/<')
]
#    path('admin/', admin.site.urls),
