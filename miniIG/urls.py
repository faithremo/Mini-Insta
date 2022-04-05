from django.urls import path, include
from miniIG import views as v

from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
)

app_name = 'miniIG'

urlpatterns = [
    #local : http://127.0.0.1:8000/
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:id>', PostDetailView.as_view(), name='post_detail'),
    path("register/", v.register, name="register"),
]

