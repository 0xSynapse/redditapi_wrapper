from django.urls import path
from .views import get_subreddit_threads

urlpatterns = [
    path('threads/', get_subreddit_threads, name='get_subreddit_threads'),
]
