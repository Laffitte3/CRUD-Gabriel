from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy

from django.views.generic import TemplateView,ListView,DetailView

from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.


class HomePageView(ListView):

    template_name="home.html"

    model=Post


class DetailPageView(DetailView):

    template_name="post_detail.html"

    model=Post

class CreatePageView(CreateView):

    template_name= "post_create.html"

    model=Post

    fields=["title","description","author"]

    success_url = reverse_lazy("home")


class UpdatePageView(UpdateView):

    template_name="post_update.html"

    model=Post

    fields=["title","description"]

    success_url = reverse_lazy("home")


class DeltePageView(DeleteView):

    template_name="post_delete.html"

    model=Post

    success_url = reverse_lazy("home")
