from django.urls import path
from . import views     # Blog app views
from .views import (
    PostListView, PostDetailView, 
    PostCreateView, PostUpdateView, 
    PostDeleteView, UserPostListView)    # Generic view classes class

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # url of blog app home page
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'), # url for blog of a user as 'user/Shubham1406/'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # url of each blog as 'post/23/'
    path('post/new/', PostCreateView.as_view(), name='post-create'), # url while creating new blog as 'post/new/'
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), # url where blog is updated as 'post/23/update'
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # url wheere blog is deleted as 'post/23/update'
    path('about/', views.about, name='blog-about'), # url of blog app about page 
]