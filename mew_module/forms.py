from django import forms
from django.db.models import fields
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(label=False)
    def clean_email(self):
        raise forms.ValidationError("The word is not a palindrome")
        return data
    class Meta:
        model = Subscription
        fields = ("email",)
