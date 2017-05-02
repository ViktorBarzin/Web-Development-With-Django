from django import forms
from django.contrib.auth.models import User

from .models import Offer


# class OfferCreateModelForm(forms.ModelForm):
#     class Meta:
#         model = Offer
#         fields = ('title', 'description', 'category', 'image')

class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
                'username': ''
                }


class CreateOfferModelForm(forms.ModelForm):
    class Meta:
        model = Offer
        # exclude = ['author']
        fields = ('title', 'description', 'category', 'image')
        # fields = '__all__'


class UpdateOfferModelForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['title', 'description', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
