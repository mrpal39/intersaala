from users.models import Profile
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
# 
# class PostCreateForm(forms.ModelForm):
    
#     class Meta:
#         model = Post
#         fields = "__all__"

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['username', 'first_name','last_name', 'email']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )