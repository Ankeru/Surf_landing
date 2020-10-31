from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SubscribeForm
from .models import Client


class LandingView(TemplateView):
    template_name = "landing.html"
    form_class = SubscribeForm 
    
    def get(self, *args, **kwargs):
        return render(self.request, 'landing.html', {'form': self.form_class()})

    def post(self, *args, **kwargs):    
        form = self.form_class(self.request.POST)
        # check whether it's valid:
        if form.is_valid():
            client = Client(email=form.cleaned_data['email'])
            client.save()
            return HttpResponseRedirect('/vtest/thanks/')
        else:
            raise Http404("Data is not valid!")
    