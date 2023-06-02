from django.urls import path

from discussions import views 
from discussions.views import DiscussionDetailView , UserDiscussionListView
# from blog.views import PostCreateView, PostDetailView, UserPostListView


urlpatterns = [

    path('list/user/<str:username>/',UserDiscussionListView.as_view(),name='user-discussions-list'),
    path('create/', views.discussion_create, name='create'),
    path('<int:pk>/detail/',DiscussionDetailView.as_view(), name='discussion-detail'),
]