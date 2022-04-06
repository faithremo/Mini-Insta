
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from .models import *
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
)

# Create your views here.
@method_decorator(login_required, name='dispatch')
class PostListView(TemplateView):
    template_name = "miniIG/post_list.html"
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'
    
class PostCreateView(CreateView):
    template_name = 'miniIG/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'
    
    def form_valid(self,form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    template_name = 'miniIG/post_detail.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now())
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)
    
# def register(request):
#         if request.method == "POST":
#             form = RegisterForm(request.POST)
            
#             if form.is_valid():
#                 form.save()
                
#                 return redirect("/home")
#             else:
#                 form = RegisterForm()
#                 return render(request, "register.html", {"form":form}) 
            
            

def index(request):
    return render(request, 'index.html')

def index(request):
    # imports photos and save it in database
    miniIG = miniIG.objects.all()
    # adding context 
    ctx = {'photo':miniIG}
    return render(request, 'index.html', ctx)   
