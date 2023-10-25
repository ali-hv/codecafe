from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from .models import Comment, ReplyComment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "accepted", "created_at", "content_type", "content"]
    ordering = ["created_at"]
    actions = ["make_accepted"]

    @admin.action(description='Mark selected comments as accepted')
    def make_accepted(self, request, queryset):
        updated = queryset.update(accepted=True)
        message = f"{updated} course{(updated - 1) * 's'} was successfully marked as accepted."
        self.message_user(request,
                          ngettext(
                              message, message, updated
                          ),
                          messages.SUCCESS)


@admin.register(ReplyComment)
class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "accepted", "created_at", "comment", "content"]
    ordering = ["created_at"]
    actions = ["make_accepted"]

    @admin.action(description='Mark selected comments as accepted')
    def make_accepted(self, request, queryset):
        updated = queryset.update(accepted=True)
        message = f"{updated} course{(updated - 1) * 's'} was successfully marked as accepted."
        self.message_user(request,
                          ngettext(
                              message, message, updated
                          ),
                          messages.SUCCESS)
