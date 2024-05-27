from django.urls import path, include
from . import views
from .views import MunicipioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'municipios', MunicipioViewSet)

urlpatterns = [
    path("gerar_csv/", views.gerar_csv, name="gerar_csv"),
    path("atualizar_municipios/", views.atualizar_municipios, name="atualizar_municipios"),
    path("", include(router.urls)),
    path("exibir_municipios/", views.exibir_municipios, name="exibir_municipios"),
]
