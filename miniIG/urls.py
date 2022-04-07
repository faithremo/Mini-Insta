from django.urls import path, include, re_path
from miniIG import views as v
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from miniIG import views
from . views import *
from . import views as app_views

app_name = 'miniIG'

urlpatterns = [
     path('', views.home, name='home'),
     path('admin/', admin.site.urls),
     path('post/', views.posts, name='post'),
     path('profile/<username>', views.profile, name='profile'),
     path('comment/<int:image_id>', views.comment, name='comment'),



    ]

