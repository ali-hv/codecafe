from django.shortcuts import render
from django.db.models import Count
from courses.models import Course


def home_page(request):
    courses = Course.objects.annotate(count=Count('users')).order_by('-count')[:3]
    return render(request, 'home/index.html', {'courses': courses})


def about_page(request):
    return render(request, 'home/about.html')


def contact_page(request):
    return render(request, 'home/contact.html')
