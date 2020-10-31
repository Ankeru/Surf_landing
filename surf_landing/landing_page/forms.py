from django.forms import ModelForm
from landing_page.models import Client

class SubscribeForm(ModelForm):
    class Meta:
        model = Client
        fields = ['email']