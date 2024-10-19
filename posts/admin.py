from django.contrib import admin
from .models import CustomUser, Post, Report

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active']
    list_filter = ['is_active']
    search_fields = ['username', 'email']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Adjust list_display to match actual fields in Post model
    list_display = ['user', 'content', 'created_at']  # Ensure 'user' is a valid field
    list_filter = ['created_at']
    search_fields = ['user__username', 'content']

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    # Adjust list_display to match actual fields in Report model
    list_display = ['reporter', 'post', 'report_type', 'report_message', 'reported_at']  # Ensure these fields are valid
    list_filter = ['report_type', 'reported_at']  # Make sure these fields exist in the model
