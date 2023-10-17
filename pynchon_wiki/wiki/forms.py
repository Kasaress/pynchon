from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    username = forms.CharField(
        max_length=50
    )
    email = forms.EmailField(
        max_length=150
    )
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=2000
    )
    file = forms.FileField(
        required=False,
    )
    captcha = CaptchaField()
