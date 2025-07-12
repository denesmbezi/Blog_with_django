# blogapp/urls.py
from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    # Home page - list all posts
    path('', views.home, name='home'),
    
    # Post detail page - individual post view
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    
    # Create new post (optional - for frontend creation)
    path('create/', views.create_post, name='create_post'),
    
    # Edit post (optional)
    path('post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    
    # Delete post (optional)
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    
    # Posts by author
    path('author/<str:username>/', views.posts_by_author, name='posts_by_author'),
]