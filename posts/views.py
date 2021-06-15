from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"

class AboutView(TemplateView):
    template_name = "about.html"
