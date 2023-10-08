from django.shortcuts import render
from courses.models import Course


def user_profile(request):
    return render(request, 'users/dashboard.html')


def user_courses(request):
    courses = Course.objects.filter(users=request.user)
    context = {'courses': courses}
    return render(request, 'users/courses.html', context=context)
