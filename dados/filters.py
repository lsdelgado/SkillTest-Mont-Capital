import django_filters
from .models import Municipio


class MunicipioFilter(django_filters.FilterSet):
    uf_sigla = django_filters.CharFilter(field_name="uf_sigla", lookup_expr="iexact")

    class Meta:
        model = Municipio
        fields = ["uf_sigla"]
