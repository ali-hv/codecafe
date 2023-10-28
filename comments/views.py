from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from .models import Comment, ReplyComment
from django.shortcuts import redirect, get_object_or_404
from urllib.parse import unquote
from courses.models import Course
from blog.models import Article


def submit_comment(request):
    referer = request.META.get('HTTP_REFERER')
    slug = unquote(referer.split('/')[4])
    if '/courses/' in referer:
        app_label = 'courses'
        model = 'course'
        object_id = get_object_or_404(Course, slug=slug).id
    elif '/articles/' in referer:
        app_label = 'blog'
        model = 'article'
        object_id = get_object_or_404(Article, slug=slug).id
    else:
        app_label = model = object_id = None

    data = dict(**request.POST)
    user_id = request.user.id
    content = data['content'][0]
    content_type_id = get_object_or_404(ContentType, app_label=app_label, model=model).id
    comment = Comment(user_id=user_id, content=content, content_type_id=content_type_id, object_id=object_id)
    comment.save()

    messages.success(request, 'نظر شما ارسال شد و پس از بررسی منتشر می شود')
    return redirect(request.META.get('HTTP_REFERER'))


def submit_reply_comment(request):
    data = dict(**request.POST)
    user_id = request.user.id
    content = data['content'][0]
    comment_id = data['comment'][0]
    reply = ReplyComment(user_id=user_id, content=content, comment_id=comment_id)
    reply.save()

    messages.success(request, 'نظر شما ارسال شد و پس از بررسی منتشر می شود')
    return redirect(request.META.get('HTTP_REFERER'))
