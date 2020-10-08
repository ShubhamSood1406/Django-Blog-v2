from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # Generic Views to add functionality to Blog Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   # login required to create post & UserPassestestMixin to update their own Post
from .models import Post
from django.contrib.auth.models import User
#from django.http import HttpResponse

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# Generic view for all Post list
class PostListView(ListView):
    model = Post        # model usage to display the blog
    template_name = 'blog/home.html'    # to use template of home
    context_object_name = 'posts'       # to use posts context to display all blogs
    ordering = ['-date_posted']     # newer to older post
    paginate_by = 5     # to display n Blog on one page

# Generic view for all Post of a particular User
class UserPostListView(ListView):
    model = Post        # model usage to display the blog
    template_name = 'blog/user_posts.html'    # to use template of home
    context_object_name = 'posts'       # to use posts context to display all blogs
    paginate_by = 5     # to display n Blog on one page

    # to modify the query set that above code return
    def get_queryset(self):    # to filter Post of a User
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# Generic view to display a single blog
class PostDetailView(DetailView):       # uses post_detail.html
    model = Post        

# Generic view to create blog
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']        # what field to entered while creating

    def form_valid(self, form):     # to set author as the current user of form.
        form.instance.author = self.request.user
        return super().form_valid(form)


# Generic view to Update blog
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']        # what field to entered while creating

    def form_valid(self, form):     # to set author as the current user of the post update form.
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):        # to check if the author is only permit to update the Blog
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Generic view to Delete blog
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'       # to redirect to home route after Blog gets deleted

    def test_func(self):        # to check if the author is only permit to Delete the Blog
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    