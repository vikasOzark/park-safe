from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . import forms
from django.contrib.auth.views import LoginView, LogoutView
from . import models

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'core_module/index.html')

class RegisterView(View):
    def get(self, request):
        template_name = 'core_module/register.html'
        context = {
            'form' : forms.RegistrationForm()
        }
        return render(request, template_name, context)

    def post(self, request):
        template_name = 'core_module/index.html'
        form = forms.RegistrationForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            auth_user = authenticate(
                username = form.cleaned_data['email'],
                password = form.cleaned_data['password1']
            )
            auth_login(request, auth_user)
            return redirect('/')
        
        return render(request, template_name)

class LoginView(LoginView):
    template_name = 'core_module/login.html'
    form_class = forms.MyLoginForm
    success_url = 'index'

class LandingPageView(View):
    def get(self, request, uuid=None):
        print(uuid)
        if uuid is not None:
            details = models.User.objects.get(uuid = uuid)
            print(details)
        else:
            details = None
            print('in none',details)
        
        template_name = 'core_module/landing_page.html'
        print('before', details)
        return render(request, template_name, {'details' : details})