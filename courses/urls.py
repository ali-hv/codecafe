from django.urls import path, re_path
from .views import courses_list, course_detail, register_course

app_name = 'courses'

urlpatterns = [
    path('', courses_list, name="courses_list"),
    re_path(r'(?P<course_slug>[-\w]+)/', course_detail, name="course_detail"),
    path('register/<int:course_id>', register_course, name='register_course'),
]
