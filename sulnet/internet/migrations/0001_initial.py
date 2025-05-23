# Generated by Django 5.0 on 2025-04-29 00:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do cliente', max_length=100, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Nome')),
                ('cpf', models.CharField(help_text='CPF do cliente', max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)], verbose_name='CPF')),
                ('endereco', models.CharField(help_text='Endereço do cliente', max_length=100, validators=[django.core.validators.MinLengthValidator(20), django.core.validators.MaxLengthValidator(100)], verbose_name='Endereço')),
                ('cidade', models.CharField(help_text='Cidade do cliente', max_length=50, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(50)], verbose_name='Cidade')),
                ('estado', models.CharField(help_text='Sigla do Estado do cliente', max_length=2, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(2)], verbose_name='Estado')),
                ('telefone', models.CharField(help_text='Telefone do cliente', max_length=20, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(20)], verbose_name='Telefone')),
                ('email', models.EmailField(help_text='Email do cliente', max_length=100, validators=[django.core.validators.MinLengthValidator(20), django.core.validators.MaxLengthValidator(100)], verbose_name='Email')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('tipo', models.CharField(choices=[('BSC', 'Básico'), ('PDR', 'Padrão'), ('PRM', 'Premium'), ('MSR', 'Master')], default='', help_text='Selecione o tipo de plano', max_length=3, verbose_name='Tipo de plano')),
                ('descricao', models.CharField(blank=True, help_text='Descreva (Opcional)', max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(20), django.core.validators.MaxLengthValidator(200)], verbose_name='Descrição')),
                ('mensalidade', models.DecimalField(decimal_places=2, help_text='Valor mensalidade', max_digits=3, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Mensalidade')),
                ('download', models.IntegerField(default='', help_text='Número de downloads', validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10000)], verbose_name='Downloads')),
                ('upload', models.IntegerField(default='', help_text='Número de uploads', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)], verbose_name='Uploads')),
                ('franquia_dados', models.IntegerField(default='', help_text='Franquia de dados', validators=[django.core.validators.MinValueValidator(50)], verbose_name='Franquia de dados')),
                ('fidelidade', models.DateField(help_text='Tempo de fidelidade', verbose_name='Fidelidade')),
                ('habilitado', models.BooleanField(help_text='Habilitado', verbose_name='Habilitado')),
                ('contratacao', models.DateField(auto_now_add=True, help_text='Data da contratação', verbose_name='Data da contratação')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='internet.cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
