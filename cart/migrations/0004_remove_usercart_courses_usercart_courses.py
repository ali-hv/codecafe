# Generated by Django 4.2.5 on 2023-11-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
        ("cart", "0003_remove_usercart_courses_usercart_courses"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usercart",
            name="courses",
        ),
        migrations.AddField(
            model_name="usercart",
            name="courses",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="cart_courses",
                to="courses.course",
            ),
        ),
    ]