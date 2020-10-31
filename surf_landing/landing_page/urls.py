from django.urls import path

from django.views.generic import TemplateView
from landing_page.views import LandingView

from . import views

urlpatterns = [    
    path('landing/', LandingView.as_view()),
    # path('thanks/', TemplateView.as_view(template_name="thanks.html")),
]