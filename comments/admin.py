from django.contrib import admin
from .models import Comment, ReplyComment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "accepted", "created_at", "content_type"]
    ordering = ["created_at"]


@admin.register(ReplyComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "accepted", "created_at", "comment"]
    ordering = ["created_at"]
