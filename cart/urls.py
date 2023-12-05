from django.urls import path, re_path
from .views import add_to_cart, cart, pay, delete_course_from_cart

app_name = 'cart'

urlpatterns = [
    path("", cart, name="cart"),
    path("pay", pay, name="pay"),
    path("add-to-cart/<int:course_id>", add_to_cart, name="add_to_cart"),
    path("delete-course-from-cart/", delete_course_from_cart, name="delete_course_from_cart"),
]
