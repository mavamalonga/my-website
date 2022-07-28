from django.forms import ModelForm
from APIREST.models import Message


class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'mail', 'message']
