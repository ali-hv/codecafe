from django.db import models
from accounts.models import CustomUser
from courses.models import Course


class CartCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class UserCart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    courses = models.ForeignKey(CartCourse, on_delete=models.CASCADE, blank=True, )

    def get_payable_amount(self):
        amount = 0
        for cart_course in self.courses.all():
            amount += cart_course.course.price

        return amount
