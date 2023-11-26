from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from centros_proteccion.forms.base import RepresentanteLegalForm
from centros_proteccion.models import RepresentanteLegal
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'home/page-404.html', status=404)


class IndexTemplate(LoginRequiredMixin, generic.TemplateView):
    template_name = "centros_proteccion/test.html"

class UsuarioRegistroMixin:
    def form_valid(self, form):
        form.instance.usuario_registro = self.request.user
        form.instance.creado = timezone.now()
        return super().form_valid(form)


class RepresentanteLegalCreateView(UsuarioRegistroMixin, LoginRequiredMixin, generic.CreateView):
    model = RepresentanteLegal
    form_class = RepresentanteLegalForm
    template_name = 'centros_proteccion/base/representante_legal/create.html'
    permission_required = 'centros_proteccion.crear_representante_legal'
    success_url = reverse_lazy('representante_legal_list')


class RepresentanteLegalListView(LoginRequiredMixin, generic.ListView):
    model = RepresentanteLegal
    template_name = 'centros_proteccion/base/representante_legal/list.html'
    permission_required = 'centros_proteccion.ver_representante_legal'
    context_object_name = 'representantes_legales'
    paginate_by = 2


