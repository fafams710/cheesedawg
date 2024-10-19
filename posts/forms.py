from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from .models import Post
class CustomUserCreationForm(UserCreationForm):
    contact_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'contact_number', 'password1', 'password2')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content']  # Make sure 'title' is included here