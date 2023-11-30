from django.conf import settings
from django.db import models

from courses.models import Course


class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_cart")
    courses = models.ManyToManyField(Course, blank=True, related_name="cart_courses")

    def get_payable_amount(self):
        amount = 0
        for cart_course in self.courses.all():
            amount += cart_course.price

        return amount
