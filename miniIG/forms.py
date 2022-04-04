from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post', 'Post', css_class='btn-primary'))
    
    class Meta:
        model = Post
        fields = [
            'image',
            'caption'
        ]
        
class RegisterForm(UserCreationForm):
        email = forms.EmailField()
        class Meta:
            model = User
            fields = ["username", "email", "password1", "password2"]       