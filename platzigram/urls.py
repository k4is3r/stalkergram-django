""" Platzi URL"""
#Django
from django.contrib import admin
from django.urls import path

#Local
from platzigram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sorted_int),
    path('hi/<str:name>/<int:age>', local_views.say_hi),
    path('posts/', posts_views.list_posts),
    path('admin/', admin.site.urls),
]
#    path('admin/', admin.site.urls),
