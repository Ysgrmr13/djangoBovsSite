from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView ,CreateView,DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post
# Create your views here.

class UserPostListView(ListView):
    model = Post
    # context_object_name = 'blog_post_user_list'
    template_name = 'blog/user_post.html'
    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Post.objects.filter(author=user)  
        context = super().get_context_data(**kwargs)
        context['blog_post_user_list'] = queryset.order_by('-date_created')
        return context
    
class PostCreateView(LoginRequiredMixin, CreateView):
      model = Post
      fields = ['title', 'content']
      
      def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
      
class PostDetailView(DetailView):
    model = Post
    #template_name = "blog/post_detail.html"
    context_object_name = 'blog_post_detail'