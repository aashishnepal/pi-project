
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
   
   
]