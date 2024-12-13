from django.shortcuts import render
from django.views.generic import ListView

from .models import Curso


class IndexView(ListView):
    template_name = "cursos/curso_list.html"
    paginate_by = 10
    allow_empty = True

    def get_queryset(self):
        return Curso.get_cursos_validos()


def ver_detalhes_curso(request):
    pass
