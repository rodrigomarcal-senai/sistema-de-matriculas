from django.db import models


class Coordenacao(models.Model):
    cod_coordenacao = models.AutoField(primary_key=True)
    cod_diretoria = models.ForeignKey(
        "Diretoria", on_delete=models.SET_NULL, db_column="cod_diretoria"
    )
    nome_coordenacao = models.CharField(max_length=50, blank=True, null=True)
    nome_responsavel = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "coordenacao"


class Curso(models.Model):
    cod_curso = models.AutoField(primary_key=True)
    cod_coordenacao = models.ForeignKey(
        "Coordenacao", on_delete=models.SET_NULL, db_column="cod_coordenacao"
    )
    nome_curso = models.CharField(max_length=50, blank=True, null=True)
    informacoes_curso = models.CharField(max_length=100, blank=True, null=True)
    ementa = models.CharField(max_length=800, blank=True, null=True)
    objetivo = models.CharField(max_length=255, blank=True, null=True)
    conteudo_programatico = models.CharField(max_length=1200, blank=True, null=True)
    metodologia = models.CharField(max_length=1200, blank=True, null=True)
    recursos_utilizados = models.CharField(max_length=500, blank=True, null=True)
    sistematica_avaliacao = models.CharField(max_length=255, blank=True, null=True)
    referencias = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "curso"


class Diretoria(models.Model):
    cod_diretoria = models.AutoField(primary_key=True)
    nome_diretoria = models.CharField(max_length=50, blank=True, null=True)
    nome_responsavel = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "diretoria"
