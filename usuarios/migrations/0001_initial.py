# Generated by Django 5.1.4 on 2024-12-12 01:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Informe um CPF válido no formato XXX.XXX.XXX-XX', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')], verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, verbose_name='Endereço de e-mail')),
                ('is_active', models.BooleanField(default=True, verbose_name='status atividade')),
                ('is_staff', models.BooleanField(default=False, verbose_name='status funcionário')),
                ('is_superuser', models.BooleanField(default=True, verbose_name='status administrador')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuario_sistema',
                'managed': True,
            },
        ),
    ]
