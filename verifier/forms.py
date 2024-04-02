from django import forms
from .models import Signature

class SignatureVerificationForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['image']
