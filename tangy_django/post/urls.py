from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
]
