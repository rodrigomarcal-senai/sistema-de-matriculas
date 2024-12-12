from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.validators import RegexValidator


class UsuarioManager(BaseUserManager):
    def create_user(self, nome, cpf, email, password=None, **outros_campos):
        if not nome:
            raise ValueError("É necessário informar um nome")
        if not cpf:
            raise ValueError("É necessário informar um número de CPF")
        if not email:
            raise ValueError("É necessário fornecer um endereço de e-mail")
        
        email = self.normalize_email(email)

        usuario = self.model(nome=nome, cpf=cpf, email=email, **outros_campos)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, nome, cpf, email, password=None, **outros_campos):
        outros_campos.setdefault("is_staff", True)
        outros_campos.setdefault("is_superuser", True)

        if outros_campos.get("is_staff") is not True:
            raise ValueError("Usuário administrador precisa conter atributo is_staff=True")
        if outros_campos.get("is_superuser") is not True:
            raise ValueError("Usuário administrador precisa conter atributo is_superuser=True")
        
        return self.create_user(nome, cpf, email, password, **outros_campos)


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(verbose_name="Nome", max_length=254)
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=14,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{3}\.\d{3}\.\d{3}-\d{2}$",
                message="Informe um CPF válido no formato XXX.XXX.XXX-XX",
            )
        ],
    )
    email = models.EmailField(verbose_name="Endereço de e-mail", max_length=254)
    is_active = models.BooleanField(verbose_name="status atividade", default=True)
    is_staff = models.BooleanField(verbose_name="status funcionário", default=False)
    is_superuser = models.BooleanField(verbose_name="status administrador", default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["nome", "email"]

    class Meta:
        db_table = "usuario_sistema"
        managed = True

    def __str__(self):
        return self.cpf
    