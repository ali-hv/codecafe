# Generated by Django 4.2.5 on 2023-10-25 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_accepted_replycomment_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replycomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comments.comment'),
        ),
    ]
