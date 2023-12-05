from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from cart.models import UserCart
from courses.models import Course
from payment.views import go_to_gateway_view


@login_required
def add_to_cart(request, course_id):
    user_cart = get_object_or_404(UserCart, user=request.user)
    course = get_object_or_404(Course, id=course_id)
    user_cart.courses.add(course)

    return redirect('courses:course_detail', course_slug=course.slug)


@login_required
def cart(request):
    user_cart = get_object_or_404(UserCart, user=request.user)
    return render(request, 'cart/cart.html', {"cart": user_cart})


@login_required
def pay(request):
    return go_to_gateway_view(request)


@login_required
def delete_course_from_cart(request):
    if request.method == "POST":
        course_id = request.POST.get('course_id')
        user_cart = get_object_or_404(UserCart, user=request.user)
        course = get_object_or_404(Course, id=course_id)
        user_cart.courses.remove(course)
        user_cart.save()

        return JsonResponse({'message': 'Course removed successfully'})

    return JsonResponse({'message': 'Invalid request method'}, status=400)
