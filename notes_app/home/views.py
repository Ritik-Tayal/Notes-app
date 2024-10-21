from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='home/signup.html'
    success_url='user/notes'

class LoginInterfaceView(LoginView):
    template_name='home/login.html'
    

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'

def home(request):
    return render(request,'home/homepage.html',{})