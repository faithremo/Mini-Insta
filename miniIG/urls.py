from django.urls import path, include
from .views import (
    PostListView,
    PostCreateView,
)

app_name = 'miniIG'

urlpatterns = [
    #local : http://127.0.0.1:8000/
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
]