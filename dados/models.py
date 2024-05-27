from django.db import models

class Municipio(models.Model):

    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    microrregiao_nome = models.CharField(max_length=200)
    mesorregiao_nome = models.CharField(max_length=200)
    uf_sigla = models.CharField(max_length=2)
    uf_nome = models.CharField(max_length=200)
    regiao_nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
