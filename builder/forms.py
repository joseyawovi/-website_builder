from django import forms
from .models import BusinessDetails

class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = BusinessDetails
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your business name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description'}),
        }
