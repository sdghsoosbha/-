from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from polls.models import Question


# Create your views here.

class theme(generic.TemplateView):
    template_name = "theme.html"