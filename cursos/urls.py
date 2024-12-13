from django.urls import path

from . import views

app_name = "cursos"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]