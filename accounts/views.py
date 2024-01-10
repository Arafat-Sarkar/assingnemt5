from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
 
class UserRegistrationView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')  
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('home')



class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')