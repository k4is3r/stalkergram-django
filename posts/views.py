#Django modules 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Forms
from posts.forms import PostForm
#models
from posts.models import Post

''' old data used
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
'''

class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(
        request = request,
        template_name = 'posts/new.html',
        context ={
            'form' : form,
            'user' : request.user,
            'profile': request.user.profile
        }
    )