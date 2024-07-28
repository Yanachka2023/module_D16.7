from django import forms
from .models import Advertisement, UserResponse


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['author', 'subject', 'category', 'description']




class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['commentator', 'advertisement', 'subject', 'description',]



