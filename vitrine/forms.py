# application/forms.py
from django import forms
from APIREST.models import Customer

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['firstname', 'name', 'email']

    widgets = {
        'firstname': forms.TextInput(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'})
    }