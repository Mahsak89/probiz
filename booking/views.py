from django.views.generic import TemplateView, View, ListView, UpdateView
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = "index.html"
