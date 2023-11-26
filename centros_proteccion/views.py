from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexTemplate(LoginRequiredMixin, generic.TemplateView):
    template_name = "centros_proteccion/test.html"


