from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from centros_proteccion.forms.base import RepresentanteLegalForm
from centros_proteccion.models import RepresentanteLegal
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

def custom_404(request, exception):
    return render(request, 'home/page-404.html', status=404)


class IndexTemplate(LoginRequiredMixin, generic.TemplateView):
    template_name = "centros_proteccion/test.html"


class UsuarioCrearRegistroMixin:
    def form_valid(self, form):
        form.instance.usuario_registro = self.request.user
        form.instance.creado = timezone.now()
        return super().form_valid(form)

class UsuarioActualizarRegistroMixin:
    def form_valid(self, form):
        form.instance.usuario_registro = self.request.user
        form.instance.actualizado = timezone.now()
        return super().form_valid(form)

class NoGuardarCacheMixin:
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@method_decorator(never_cache, name='dispatch')
class RepresentanteLegalCreateView(NoGuardarCacheMixin, UsuarioCrearRegistroMixin, LoginRequiredMixin, generic.FormView):
    form_class = RepresentanteLegalForm
    template_name = 'centros_proteccion/base/representante_legal/form.html'
    permission_required = 'centros_proteccion.crear_representante_legal'
    success_url = reverse_lazy('representante_legal_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RepresentanteLegalListView(NoGuardarCacheMixin, LoginRequiredMixin, generic.ListView):
    model = RepresentanteLegal
    template_name = 'centros_proteccion/base/representante_legal/list.html'
    permission_required = 'centros_proteccion.ver_representante_legal'
    context_object_name = 'representantes_legales'
    paginate_by = 5


class RepresentanteLegalUpdateView(NoGuardarCacheMixin, UsuarioActualizarRegistroMixin, LoginRequiredMixin, generic.UpdateView):
    model = RepresentanteLegal
    form_class = RepresentanteLegalForm
    template_name = 'centros_proteccion/base/representante_legal/form.html'
    permission_required = 'centros_proteccion.modificar_representante_legal'
    success_url = reverse_lazy('representante_legal_list')



class RepresentanteLegalDetailView(NoGuardarCacheMixin, LoginRequiredMixin, generic.DetailView):
    model = RepresentanteLegal
    template_name = 'centros_proteccion/base/representante_legal/detail.html'
    permission_required = 'centros_proteccion.ver_representante_legal'
    context_object_name = 'representante_legal'

    def get_context_data(self, **kwargs):
        # mencionar cuantas razones sociales tiene el representante legal
        context = super().get_context_data(**kwargs)
        context['razones_sociales'] = self.object.razon_social.count()
        return context


class RepresentanteLegalDeleteView(NoGuardarCacheMixin, LoginRequiredMixin, generic.DeleteView):
    model = RepresentanteLegal
    template_name = 'centros_proteccion/base/representante_legal/confirm_delete.html'
    permission_required = 'centros_proteccion.eliminar_representante_legal'
    success_url = reverse_lazy('representante_legal_list')

