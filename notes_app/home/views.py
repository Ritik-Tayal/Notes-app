from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='home/signup.html'
    success_url=reverse_lazy('login')
    
    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('user/notes')
        return super().get(request,*args,**kwargs)

class LoginInterfaceView(LoginView):
    template_name='home/login.html'
    

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'

def home(request):
    return render(request,'home/homepage.html',{})