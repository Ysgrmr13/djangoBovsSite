=======
# djangoBovsSite
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
```
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
```
=======

#[pytest]
DJANGO_SETTINGS_MODULE = djangoBovsSite.settings
python_files = tests.py test_*.py *_tests.py
>>>>>>> 37119c3742eb0062d2464d7928a45b7d226a32e3
