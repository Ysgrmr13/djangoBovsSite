from django.urls import path
from blog.views import PostCreateView, PostDetailView, UserPostListView


urlpatterns = [

    path('post/user/<str:username>/', UserPostListView.as_view(), name='user-post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
]