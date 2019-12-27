from django.urls import path

from . import views


urlpatterns = [
   path('', views.LoginPageView.as_view(), name='login'),

   path('home/', views.HomePageView.as_view(), name='home'),

   path('about/', views.AboutPageView.as_view(), name='about'),

]

