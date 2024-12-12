from django.urls import path

from . import views

app_name = "usuarios"
urlpatterns = [
    path("cadastro/", views.cadastrar_usuario, name="cadastro"),
    path("login/", views.login_usuario, name="login"),
]
