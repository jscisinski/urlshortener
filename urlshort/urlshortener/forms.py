from django import forms
from django.core.exceptions import ValidationError
from .models import Shortener


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"placeholder": "Your URL to shorten"}))

    class Meta:
        model = Shortener
        fields = ('long_url',)
