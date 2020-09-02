from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserChangeForm


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfilePictureUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

