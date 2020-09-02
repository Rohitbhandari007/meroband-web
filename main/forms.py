from django import forms
from django.contrib.auth.models import User
from .models import Post


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['content', 'videos']