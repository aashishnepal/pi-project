from django.views.generic import TemplateView

from .models import website

class LoginPageView(TemplateView):
    model = website
    template_name ='registration/login.html'

class HomePageView(TemplateView):
    template_name ='home.html'



class AboutPageView(TemplateView):
    template_name ='about.html'

