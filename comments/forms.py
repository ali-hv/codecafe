from django import forms
from .models import Comment, ReplyComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ['content']
