from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from mysite.models import TimeStampedModel
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from comments.models import Comment


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Teacher Bio")

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=250, blank=False, verbose_name='Video Title')
    video = models.FileField(upload_to='videos/courses/%Y-%m-%d/', verbose_name='Video File')  # TODO add file validator
    uploaded_date = models.DateTimeField(auto_now=True)
    sequence_number = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, default=None)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="video_course") # Just for easier managing

    def __str__(self):
        return self.title


class Course(TimeStampedModel):
    STATUS_CHOICES = (('going', 'Going On'), ('done', 'Done'))

    title = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(unique=True, max_length=255, allow_unicode=True)
    detail = models.TextField()
    image = models.ImageField(upload_to='photos/courses/%Y-%m-%d/')
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=0)
    status = models.CharField(max_length=8, default='Going On', choices=STATUS_CHOICES)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    videos = models.ManyToManyField(Video, blank=True, related_name="course_videos")
    users = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title

    def get_final_price(self):
        return int(self.price * (100 - self.discount) / 100)

