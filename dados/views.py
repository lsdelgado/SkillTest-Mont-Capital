from django.shortcuts import render
import pandas
import requests
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Municipio
from .serializers import MunicipioSerializer
from .filters import MunicipioFilter
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


def atualizar_municipios(request):
    
    response = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/municipios")

    if response.status_code == 200:
        municipios_json = response.json()
        municipios_formatted = pandas.json_normalize(municipios_json, max_level=5)

        Municipio.objects.all().delete()

        municipios_list = []
        for _, row in municipios_formatted.iterrows():
            municipio = Municipio(
                id=row["id"],
                nome=row["nome"],
                microrregiao_nome=row["microrregiao.nome"], 
                mesorregiao_nome=row["microrregiao.mesorregiao.nome"],
                uf_sigla=row["microrregiao.mesorregiao.UF.sigla"],
                uf_nome=row["microrregiao.mesorregiao.UF.nome"],
                regiao_nome=row["microrregiao.mesorregiao.UF.regiao.nome"],
            )
            municipios_list.append(municipio)

        Municipio.objects.bulk_create(municipios_list)

        return JsonResponse(
            {
               "status": "success",
                "message": "Dados de municípios atualizados com sucesso.",
            }
        )
    
    else:
        return JsonResponse(
            {
                "status": "error",
                "message": f"Erro na requisição: {response.status_code}",
            }
        )


def gerar_csv(request):

    municipios = Municipio.objects.all().values()
    df_municipios = pandas.DataFrame(municipios)

    csv_file_path = "Municipios.csv"
    df_municipios.to_csv(csv_file_path, index=True, encoding="utf-8")

    return HttpResponse("Arquivo gerado com sucesso")


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MunicipioFilter


def exibir_municipios(request):
    estados = [
        {"nome": "Acre", "sigla": "AC"},
        {"nome": "Alagoas", "sigla": "AL"},
        {"nome": "Amapá", "sigla": "AP"},
        {"nome": "Amazonas", "sigla": "AM"},
        {"nome": "Bahia", "sigla": "BA"},
        {"nome": "Ceará", "sigla": "CE"},
        {"nome": "Distrito Federal", "sigla": "DF"},
        {"nome": "Espírito Santo", "sigla": "ES"},
        {"nome": "Goiás", "sigla": "GO"},
        {"nome": "Maranhão", "sigla": "MA"},
        {"nome": "Mato Grosso", "sigla": "MT"},
        {"nome": "Mato Grosso do Sul", "sigla": "MS"},
        {"nome": "Minas Gerais", "sigla": "MG"},
        {"nome": "Pará", "sigla": "PA"},
        {"nome": "Paraíba", "sigla": "PB"},
        {"nome": "Paraná", "sigla": "PR"},
        {"nome": "Pernambuco", "sigla": "PE"},
        {"nome": "Piauí", "sigla": "PI"},
        {"nome": "Rio de Janeiro", "sigla": "RJ"},
        {"nome": "Rio Grande do Norte", "sigla": "RN"},
        {"nome": "Rio Grande do Sul", "sigla": "RS"},
        {"nome": "Rondônia", "sigla": "RO"},
        {"nome": "Roraima", "sigla": "RR"},
        {"nome": "Santa Catarina", "sigla": "SC"},
        {"nome": "São Paulo", "sigla": "SP"},
        {"nome": "Sergipe", "sigla": "SE"},
        {"nome": "Tocantins", "sigla": "TO"},
    ]
    return render(request, "municipios.html", {"estados": estados})
