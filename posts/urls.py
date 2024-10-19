
from django.urls import path
from .views import post_list
from .views import post_list, create_post, login_view, register, logout_view,
app_name = 'posts'
urlpatterns = [
    path('', post_list, name='post_list'),  # Home route for post listing
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-post/', create_post, name='create_post'),  # Add this line
    path('posts/', post_list, name='post_list'),  # List all posts
    path('posts/create/', create_post, name='create_post'),  # Create a new post
    path('register/', register, name='register'),  # Include URLs from posts app
]