from django import forms
from APIREST.models import MyModel, MYCHOICES

class MyForm(forms.ModelForm):
    myfield = forms.MultipleChoiceField(choices=MYCHOICES, widget=forms.SelectMultiple)
    class Meta:
        model = MyModel