from django import forms
from django.forms.widgets import Textarea


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100, required=True)
    subject = forms.CharField(max_length=100, required=True)
    body = forms.CharField(widget=forms.Textarea,
                           max_length=2000, required=True)

    def __str__(self) -> str:
        return super().__str__()