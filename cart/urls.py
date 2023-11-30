from django.urls import path, re_path
from .views import add_to_cart

app_name = 'cart'

urlpatterns = [
    path("add-to-cart/<int:course_id>", add_to_cart, name="add_to_cart")
]
