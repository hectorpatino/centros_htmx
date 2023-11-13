from django.shortcuts import render
from django.views import generic
# Create your views here.


class IndexTemplate(generic.TemplateView):
    template_name = "centros_proteccion/test.html"