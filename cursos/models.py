from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.urls import reverse


class Diretoria(models.Model):
    cod_diretoria = models.AutoField(primary_key=True)
    nome_diretoria = models.CharField(max_length=50, blank=True, null=True)
    nome_responsavel = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "diretoria"


class Coordenacao(models.Model):
    cod_coordenacao = models.AutoField(primary_key=True)
    cod_diretoria = models.ForeignKey(
        Diretoria,
        on_delete=models.DO_NOTHING,
        db_column="cod_diretoria",
    )
    nome_coordenacao = models.CharField(max_length=50, blank=True, null=True)
    nome_responsavel = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "coordenacao"


class Curso(models.Model):
    cod_curso = models.AutoField(primary_key=True)
    cod_coordenacao = models.ForeignKey(
        Coordenacao,
        on_delete=models.DO_NOTHING,
        db_column="cod_coordenacao",
    )
    nome_curso = models.CharField(max_length=50, blank=True, null=True)
    informacoes_curso = models.TextField(max_length=100, blank=True, null=True)
    ementa = models.TextField(max_length=800, blank=True, null=True)
    objetivo = models.TextField(max_length=255, blank=True, null=True)
    conteudo_programatico = models.TextField(max_length=1200, blank=True, null=True)
    metodologia = models.TextField(max_length=1200, blank=True, null=True)
    recursos_utilizados = models.TextField(max_length=500, blank=True, null=True)
    sistematica_avaliacao = models.TextField(max_length=255, blank=True, null=True)
    referencias = models.TextField(max_length=300, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        managed = True
        db_table = "curso"

    @classmethod
    def get_cursos_validos(cls):
        return cls.objects.exclude(
            Q(nome_curso__isnull=True) | Q(nome_curso__exact=""),
            Q(informacoes_curso__isnull=True) | Q(informacoes_curso__exact=""),
            Q(ementa__isnull=True) | Q(ementa__exact=""),
            Q(conteudo_programatico__isnull=True) | Q(conteudo_programatico__exact=""),
            Q(metodologia__isnull=True) | Q(metodologia__exact=""),
        )

    def __str__(self):
        return self.nome_curso

    def get_absolute_url(self):
        return reverse("detalhes_curso", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome_curso)
        return super().save(*args, **kwargs)
 
