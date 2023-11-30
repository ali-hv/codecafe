from django.contrib import admin
from cart.models import UserCart


@admin.register(UserCart)
class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "get_payable_amount", ]
