from django.shortcuts import render
from django.views.generic import ListView

from .models import Curso


class IndexView(ListView):
    template_name = "cursos/curso_list.html"
    paginate_by = 10
    model = Curso
