from dataclasses import field
from xml.etree.ElementTree import Comment
from django import forms
from .models import Comments, Post, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm


class PostForm(ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post', 'Post', css_class='btn-primary'))
    
    class Meta:
        model = Post
        fields = [
            'image',
            'caption',
            'name'
            
        ]
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile']
        
        
class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
                
          
        
class RegisterForm(UserCreationForm):
        email = forms.EmailField()
        class Meta:
            model = User
            fields = ["username", "email", "password1", "password2"]       