from django.urls import path
from .views import user_profile, user_courses

app_name = 'users'

urlpatterns = [
    path('profile', user_profile, name="user_profile"),
    path('courses', user_courses, name="user_courses"),
]
