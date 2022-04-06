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
    #local : http://127.0.0.1:8000/
    path('',login_required(PostListView.as_view(), login_url='/login/')),
    #path('page/', LoginRequiredView.as_view()),
    #path('page/', login_required(LoginRequiredView.as_view()
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:id>', PostDetailView.as_view(), name='post_detail'),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    re_path('accounts/', include('django_registration.backends.one_step.urls')),
    re_path('accounts/register/',
        RegistrationView.as_view(success_url='/profile/'),
        name='django_registration_register'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

]

