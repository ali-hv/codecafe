# Generated by Django 4.2.5 on 2023-10-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_course_discount_alter_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
