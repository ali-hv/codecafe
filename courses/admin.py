from django.contrib import admin
from .models import Course, Category, Video, Teacher
from django.contrib import messages
from django.utils.translation import ngettext


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "updated_date", "is_published", "teacher", ]
    list_filter = ["is_published", "category", "updated_date", "status", ]
    ordering = ["updated_date", ]
    actions = ["make_published", "make_done", ]

    @admin.action(description='Mark selected courses as published')
    def make_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        message = f"{updated} course{(updated-1) * 's'} was successfully marked as published."
        self.message_user(request,
                          ngettext(
                              message, message, updated
                          ),
                          messages.SUCCESS)

    @admin.action(description='Mark selected courses as done')
    def make_done(self, request, queryset):
        updated = queryset.update(status='done')
        message = f"{updated} course{(updated-1) * 's'} was successfully marked as done."
        self.message_user(request,
                          ngettext(
                              message, message, updated
                          ),
                          messages.SUCCESS)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["course", "sequence_number", "title", "video", "uploaded_date", ]
    list_filter = ["course", ]
    ordering = ['sequence_number', ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", ]
