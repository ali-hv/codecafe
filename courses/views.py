from django.shortcuts import render, get_object_or_404, redirect
from .models import Course


def courses_list(request):
    courses = Course.objects.filter(is_published=True)
    context = {'courses': courses}

    return render(request, 'courses/index.html', context=context)


def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)

    if request.user not in course.users.all():
        context = {'course': course, 'access': False}
    else:
        context = {'course': course, 'access': True}

    return render(request, 'courses/course.html', context=context)


def register_course(request, course_id):
    if request.user.is_authenticated:
        course_user_field = get_object_or_404(Course, id=course_id)
        course_user_field.users.add(request.user)
        return redirect('courses:course_detail', course_slug=course_user_field.slug)
    else:
        return redirect('home:register')
