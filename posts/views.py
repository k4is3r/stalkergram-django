from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime


posts = [
    {
        'name':'Mont Blac',
        'user':'Yesica Cortes',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036'
    },    
    {
        'name':'Via Lactea',
        'user':'C. Vander',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H hrs'),
        'picture':'https://picsum.photos/200/200/?image=903'
    },    
    {
        'name':'Nuevo auditorio',
        'user':'Thespinartist',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H hrs'),
        'picture':'https://picsum.photos/200/200/?image=1076'
    }
]

def list_posts(request):
    return render(request, 'feed.html')