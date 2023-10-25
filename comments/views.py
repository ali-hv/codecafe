from django.contrib.contenttypes.models import ContentType
from .models import Comment, ReplyComment
from django.shortcuts import redirect


def submit_comment(request):
    data = dict(**request.POST)
    user_id = data['user'][0]
    content = data['content'][0]
    app_label = data['app_label'][0]
    model = data['model'][0]
    content_type_id = ContentType.objects.get(app_label=app_label, model=model).id
    object_id = data['object_id'][0]
    comment = Comment(user_id=user_id, content=content, content_type_id=content_type_id, object_id=object_id)
    comment.save()
    return redirect(request.META.get('HTTP_REFERER'))


def submit_reply_comment(request):
    data = dict(**request.POST)
    user_id = data['user'][0]
    content = data['content'][0]
    comment_id = data['comment'][0]
    reply = ReplyComment(user_id=user_id, content=content, comment_id=comment_id)
    reply.save()
    return redirect(request.META.get('HTTP_REFERER'))
