from django import forms

from apps.models import Url


class UrlForm(forms.ModelForm):
    # long_name = forms.URLField(max_length=255)

    class Meta:
        model = Url
        exclude = ('short_name',)
