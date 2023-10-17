from django.urls import path, re_path
from .views import courses_list, course_detail, register_course, search_courses

app_name = 'courses'

urlpatterns = [
    path('', courses_list, name="courses_list"),
    path('register/<int:course_id>', register_course, name='register_course'),
    re_path(r'^search(?P<keyword>\w{0,50})/$', search_courses, name='search_courses'),
    re_path(r'(?P<course_slug>[-\w]+)/', course_detail, name="course_detail"),
]
