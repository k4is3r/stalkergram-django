from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime


posts = [
    {
        'title':'Mont Blac',
        'user':{
            'name':'Yesica Cortes',
            'picture':'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H hrs'),
        'photo':'https://picsum.photos/800/600/?image=1036'
    },    
    {
        'title':'Via Lactea',
        'user':{
            'name':'C. Vander',
            'picture':'https://picsum.photos/60/60/?image1005'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H hrs'),
        'photo':'https://picsum.photos/800/800/?image=903'
    },    
    {
        'title':'Nuevo auditorio',
        'user':{
            'name':'Thespinartist',
            'picture':'https://picsum.photos/60/60/?image=883'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H hrs'),
        'photo':'https://picsum.photos/500/700/?image=1076'
    },
    {
        'title':'Another World',
        'user':{
            'name':'k4is3r',
            'picture':'https://picsum.photos/60/60/?image=1006'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H hrs'),
        'photo':'https://picsum.photos/500/700/?image=1077'
    }
]

@login_required
def list_posts(request):
    return render(request, 'posts/feed.html', {'posts': posts})