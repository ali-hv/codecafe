from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from cart.models import UserCart
from courses.models import Course


@login_required
def add_to_cart(request, course_id):
    user_cart = get_object_or_404(UserCart, user=request.user)
    course = get_object_or_404(Course, id=course_id)
    user_cart.courses.add(course)

    return redirect('courses:course_detail', course_slug=course.slug)
