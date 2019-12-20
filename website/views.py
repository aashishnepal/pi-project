from django.views.generic import TemplateView

from .models import website

class HomePageView(TemplateView):
    model = website
    template_name ='home.html'


class AboutPageView(TemplateView):
    template_name ='about.html'
    
