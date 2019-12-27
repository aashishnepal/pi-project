from django.shortcuts import render, redirect
from django.views import generic

from django.views.generic import TemplateView

from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class LoginPageView(TemplateView):
    # model = accounts
    template_name ='registration/login.html'

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User = auth.authenticate(username=username ,password=password )
        
        if User is not None:
            auth.login(request, User)
            return render(request,'home.html')
        else:
            messages.info(request,'invalid credentials') 
            return render(request,'LoginPageView')  
    else:
        return render(request,'LoginPageView')


class HomePageView(TemplateView):
    template_name ='home.html'



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    