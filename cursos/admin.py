from django.contrib import admin

from .models import Curso


class CursoAdmin(admin.ModelAdmin):
    list_display = [
        "cod_coordenacao",
        "nome_curso",
        "informacoes_curso",
        "ementa",
        "objetivo",
        "conteudo_programatico",
        "metodologia",
        "recursos_utilizados",
        "sistematica_avaliacao",
        "referencias",
    ]
    prepopulated_fields = {
        "slug": [
            "nome_curso",
        ]
    }


admin.site.register(Curso, CursoAdmin)
