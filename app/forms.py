from django import forms
from .models import Utulisateur ,DIAL_CODES_CHOICES


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Utulisateur
        fields = ['phone_number_code', 'phone_number']

    phone_number_code = forms.ChoiceField(choices=DIAL_CODES_CHOICES)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Numéro de téléphone'}))
