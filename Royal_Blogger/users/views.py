from blog.models import UserProfile, Post
from .forms import RegisterForm
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

def Like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class UserRegister(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(UserRegister, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class UserEditProfile(generic.UpdateView):
    success_url = reverse_lazy('blog:home')
    template_name = 'registration/editprofile.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def get_object(self):
        return self.request.user

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(UserEditProfile, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('blog:home')

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(ChangePassword, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class EditProfilePage(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/editprofilepage.html'
    success_url = reverse_lazy('blog:home')
    fields = ['profile_pic', 'bio', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url', 'linkedin_url']

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(EditProfilePage, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class ShowProfile(DetailView):
    model = UserProfile
    template_name = 'registration/userprofile.html'

    def get_context_data(self, *args, **kwargs):
        # cat_menu = Category.objects.all()
        context = super(ShowProfile, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        # context["cat_menu"] = cat_menu
        return context



