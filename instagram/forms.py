from django import forms

from instagram.models import Feed, Comment


class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ('content', 'image')
        labels = {
            "content": '게시글 내용',
            "image": '게시글 이미지',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            "content": '답글 내용',
        }
