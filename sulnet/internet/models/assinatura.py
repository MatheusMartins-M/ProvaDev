import datetime
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from rest_framework.exceptions import ValidationError

from internet.models import Cliente
from internet.models.base_model import BaseModel
from internet.enumerations.tipo_plano import TipoPlano
from django.db import models

class Assinatura(BaseModel):
    tipo = models.CharField(
        null=False, blank=False, default="",
        max_length=3,
        choices=TipoPlano,
        help_text="Selecione o tipo de plano",
        verbose_name="Tipo de plano",
    )

    descricao = models.CharField(
        null=True, blank=True,
        max_length=200,
        validators=[MinLengthValidator(20), MaxLengthValidator(200)],
        help_text="Descreva (Opcional)",
        verbose_name="Descrição",
    )

    mensalidade = models.DecimalField(
        null=False, blank=False,
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        help_text="Valor mensalidade",
        verbose_name="Mensalidade",
    )

    download = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(10000)],
        default="",
        help_text="Número de downloads",
        verbose_name="Downloads",

    )

    upload = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000)],
        default="",
        help_text="Número de uploads",
        verbose_name="Uploads",
    )

    franquia_dados = models.IntegerField(
        validators=[MinValueValidator(50)],
        default="",
        help_text="Franquia de dados",
        verbose_name="Franquia de dados",
    )

    fidelidade = models.DateField(
        null=False, blank=False,
        help_text="Tempo de fidelidade",
        verbose_name="Fidelidade",
    )

    habilitado = models.BooleanField(
        null=False, blank=False,
        help_text="Habilitado",
        verbose_name="Habilitado",
    )

    contratacao = models.DateField(
        null=False, blank=False,
        auto_now_add=True,
        help_text="Data da contratação",
        verbose_name="Data da contratação",
    )

    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.cliente.nome} - {self.tipo}'

    #def clean(self):
    #    if self.fidelidade < datetime.date.today():
        #        raise ValidationError(
        #             {"fidelidade": "Não é possível salvar datas menores que o dia de hoje"},
        #              code="error001")
        #
        #      elif self.tipo == TipoPlano.BASIC and (self.download > 100 or self.upload > 100):
        #          raise ValidationError(
        #              {"O máximo de download ou upload foi alcançado"},
        #             code="error002"
        #   )
        #
        #elif self.tipo == TipoPlano.STANDARD and (self.download > 1000 or self.upload > 1000):
        #    raise ValidationError(
        #        {"O máximo de download ou upload foi alcançado"},
        #       code="error003"
        #   )
        #
        #elif self.tipo == TipoPlano.PREMIUM and (self.download > 5000 or self.upload > 5000):
        #    raise ValidationError(
        #        {"O máximo de download ou upload foi alcançado"},
        #        code="error004"
        #    )


        #elif self.tipo == TipoPlano.MASTER and (self.download > 10000 or self.upload > 10000):
        #    raise ValidationError(
        #        {"O máximo de download ou upload foi alcançado"},
        #        code="error005"
    #    )