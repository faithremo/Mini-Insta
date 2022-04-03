from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class PostForm(forms.ModelForm):
    helper = FormHelper()