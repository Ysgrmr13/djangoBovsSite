# from typing import Any
# from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DiscussionCreateForm
from django.contrib.auth.decorators import login_required
from .models import Discussion
from django.contrib import messages
# Create your views here.


class UserDiscussionListView(ListView):
    model = Discussion
    # context_object_name = 'blog_post_user_list'
    template_name = 'discussions/user_discussion.html'
    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Discussion.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['discussions_post_user_list'] = queryset.order_by('-date_created')
        return context


class DiscussionCreateView(LoginRequiredMixin, CreateView):
    model = Discussion
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = "discussions/discussion_detail.html"
    context_object_name = 'discussion_detail'


@login_required
def discussion_create(request):
    # если запрос Post, только тогда обрабатываем форму.
    if request.method == 'POST':
        # Создадим экземпляр формы и заполним его данными запроса (укажем параметры)
        form = DiscussionCreateForm(request.POST, request.FILES)  # данные POST для заполнения формы
        # ПРОФЕССИОНАЛЬНО СКАЗАТЬ ТАК ПРО DISCUSSIONCREATEFORM(REQUEST.POST, REQUEST.FILES)- ПРИВЯЗКА ДАННЫХ К ФОРМЕ.
        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion.author = request.user
            new_discussion.save()
            messages.success(request, 'Дискуссия добавлена')
            return redirect(new_discussion.get_absolute_url())
    else:
        # если поступит get запрос (или любой др), вернуть пустую форму.
        form = DiscussionCreateForm()
    return render(request, "discussions/create_form.html", {"form": form})
