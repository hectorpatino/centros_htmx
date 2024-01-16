import django_filters

from .models import RepresentanteLegal


class RepresentanteLegalFilter(django_filters.FilterSet):
    class Meta:
        model = RepresentanteLegal
        fields = {
            'correo': ['icontains'],
        }
