#django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, FormView, UpdateView

#models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#forms
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin,DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website','biography','phone_number','picture']
    slug_field = 'username'
    def get_objetc(self):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username})

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin,auth_views.LogoutView ):
    template_name = 'users/logged_out.html'



"""old signup method change with class view
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    return render(
        request = request,
        template_name='users/signup.html',
        context={'form' : form}
        )

@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            url = reverse('users:detail', kwargs = {'username': request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()
    return render(
        request = request,
        template_name ='users/update_profile.html',
        context={
            'profile': profile,
            'user' : request.user,
            'form' : form
        }
    )
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error':'Invalid Username and Password'})
    return render(request, 'users/login.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

"""