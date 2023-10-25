from django import forms
from .models import Comment, ReplyComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ['content']
