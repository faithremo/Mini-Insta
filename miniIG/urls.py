from django.urls import path, include, re_path
from miniIG import views as v
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from miniIG import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
)

app_name = 'miniIG'

urlpatterns = [
    path('',login_required(PostListView.as_view(), login_url='/accounts/login/')),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:id>', PostDetailView.as_view(), name='post_detail'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

]

