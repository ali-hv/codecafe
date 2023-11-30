from django.shortcuts import render, get_object_or_404, redirect
from .models import Course


def courses_list(request):
    courses = Course.objects.filter(is_published=True)
    context = {'courses': courses}

    return render(request, 'courses/index.html', context=context)


def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    course_duration = sum(video.duration for video in course.videos.all())
    course_duration = int(course_duration / 60)
    comments = course.comments.filter(accepted=True)

    context = {'course': course, 'comments': comments, 'duration': course_duration, }

    return render(request, 'courses/course.html', context=context)


def register_course(request, course_id):
    if request.user.is_authenticated:
        course_user_field = get_object_or_404(Course, id=course_id)
        course_user_field.users.add(request.user)
        return redirect('courses:course_detail', course_slug=course_user_field.slug)
    else:
        return redirect('accounts:login')


def search_courses(request, keyword):
    keyword = request.GET.get('q')
    courses = Course.objects.filter(title__contains=keyword, is_published=True)
    context = {'courses': courses}

    return render(request, 'courses/index.html', context=context)
