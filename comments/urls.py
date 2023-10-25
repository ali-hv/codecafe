from django.urls import path
from .views import submit_comment, submit_reply_comment

app_name = 'comments'

urlpatterns = [
    path('submit_comment', submit_comment, name='submit_comment'),
    path('submit_reply_comment', submit_reply_comment, name='submit_reply_comment'),
]
