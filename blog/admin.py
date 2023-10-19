from django.contrib import admin
from .models import Article, Author
from django.contrib import messages
from django.utils.translation import ngettext


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "updated_date", "is_published", "author", ]
    list_filter = ["is_published", "category", "updated_date", ]
    ordering = ["updated_date", ]
    actions = ["make_published", ]

    @admin.action(description='Mark selected articles as published')
    def make_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        message = f"{updated} article{(updated-1) * 's'} was successfully marked as published."
        self.message_user(request,
                          ngettext(
                              message, message, updated
                          ),
                          messages.SUCCESS)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["get_full_name", ]

