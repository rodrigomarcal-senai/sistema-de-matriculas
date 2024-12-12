from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Usuario


class CadastrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["nome", "cpf", "email"]


class LoginUsuarioForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ["username", "password"]
