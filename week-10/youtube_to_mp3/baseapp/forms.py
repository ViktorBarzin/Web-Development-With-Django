from django import forms


class VideoInputForm(forms.Form):
    url = forms.URLField()
    email = forms.EmailField()
