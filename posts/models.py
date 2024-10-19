from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()
class CustomUser(AbstractUser):
    # Add related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Define a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Define a unique related_name
        blank=True
    )

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)  # Allow null values
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# posts/models.py

class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure this field exists
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Ensure this field exists
    report_type = models.CharField(max_length=100)  # Example field
    report_message = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report by {self.reporter.username} on {self.post.content[:20]}'


class UserPreference(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        dark_mode = models.BooleanField(default=False)

# forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Include the fields you want in the form
