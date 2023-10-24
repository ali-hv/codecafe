from django.contrib import admin
from .models import Course, Category, Video, Teacher, Chapter
from django.contrib import messages
from django.utils.translation import ngettext
from django_summernote.admin import SummernoteModelAdmin


course_id = None


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ["title", "updated_date", "is_published", "teacher", ]
    list_filter = ["is_published", "category", "updated_date", "status", ]
    ordering = ["updated_date", ]
    actions = ["make_published", "make_done", ]
    summernote_fields = ('detail',)

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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        global course_id
        course_id = request.build_absolute_uri().split('/')[-3]
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["course", "sequence_number", "title", "uploaded_date", ]
    list_filter = ["course", ]
    ordering = ['sequence_number', ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "chapter":
            kwargs["queryset"] = Chapter.objects.filter(course_id=course_id)
        elif db_field.name == "course":
            kwargs["queryset"] = Course.objects.filter(id=course_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", ]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "course", ]