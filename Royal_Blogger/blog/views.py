from .models import Post
from .forms import PostForm
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogCategories

def Like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog:detail', args=[str(pk)]))

class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-created_on']

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(Home, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/postdetail.html'

    def get_context_data(self, *args, **kwargs):
        # cat_menu = Category.objects.all()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        # context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/addpost.html'

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(AddPost, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class EditPost(UpdateView):
    model = Post
    template_name = 'blog/editpost.html'
    fields = ['title', 'body', 'image',]

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(EditPost, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/deletepost.html'
    success_url = reverse_lazy('blog:home')

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(DeletePost, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

# class AddCategory(CreateView):
#     model = BlogCategories
#     template_name = 'blog/addcategory.html'
#     fields = '__all__'

#     def get_context_data(self, *args, **kwargs):
#         cat_menu = BlogCategories.objects.all()
#         context = super(AddCategory, self).get_context_data(*args, **kwargs)
#         context["cat_menu"] = cat_menu
#         return context

# def BlogCategory(request, cats):
#     category_posts = Post.objects.filter(category=cats)
#     return render(request, 'blog/categories.html', {'cats': cats, 'category_posts': category_posts})
    
