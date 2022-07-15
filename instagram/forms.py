from django import forms

from instagram.models import Feed


class UploadFeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ('content', 'image')
