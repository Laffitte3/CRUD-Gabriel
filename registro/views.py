from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class FirstPageView(TemplateView):


    template_name="registration/first_page.html"

class SignupPageView(CreateView):

    template_name="registration/signup.html"
    form_class= UserCreationForm
    success_url= reverse_lazy("login")

class LogoutPageView(TemplateView):

    template_name="registration/logout.html"
