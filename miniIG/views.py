
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from .models import *
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse


# Create your views here.

@login_required   
def home(request):
    form = CommentForm()
    posts = Post.all_posts()
    current_user = request.user

    if request.method =='POST':
        if 'postComment' in request.POST:
            form = CommentForm(request.POST)
            comment = form.save(commit=False)
            comment.author = current_user
            comment.save()
        
    return render(request, 'miniIG/post_list.html', {'posts':posts, 'form':form})

@login_required
def posts(request):
    if request.method == 'POST':
        current_user = request.user
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
        return HttpResponseRedirect(request.path_info)
        
    else:
        form = PostForm()
    
    
    return render(request,'miniIG/post_create.html', {'form':form})


def profile(request,username):
    user = request.user
    user = User.objects.filter(username=user.username).first()
    posts = Post.objects.filter(author=user)
    return render(request, 'miniIG/profile.html', {'user': user,'posts':posts})
