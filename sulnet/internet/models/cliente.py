from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from internet.models.base_model import BaseModel

class Cliente(BaseModel):
    nome = models.CharField(
        null=False, blank=False,
        max_length=100,
        validators=[MinLengthValidator(10)],
        help_text="Nome do cliente",
        verbose_name="Nome"
    )

    cpf = models.CharField(
        null=False, blank=False, unique=True,
        max_length=11,
        validators=[MinLengthValidator(11), MaxLengthValidator(11)],
        help_text="CPF do cliente",
        verbose_name="CPF"
    )

    endereco = models.CharField(
        null=False, blank=False,
        max_length=100,
        validators=[MinLengthValidator(20), MaxLengthValidator(100)],
        help_text="Endereço do cliente",
        verbose_name="Endereço"
    )

    cidade = models.CharField(
        null=False, blank=False,
        max_length=50,
        validators=[MinLengthValidator(3), MaxLengthValidator(50)],
        help_text="Cidade do cliente",
        verbose_name="Cidade"
    )

    estado = models.CharField(
        null=False, blank=False,
        max_length=2,
        validators=[MinLengthValidator(2), MaxLengthValidator(2)],
        help_text="Sigla do Estado do cliente",
        verbose_name="Estado"
    )

    telefone = models.CharField(
        null=False, blank=False,
        max_length=20,
        validators=[MinLengthValidator(10), MaxLengthValidator(20)],
        help_text="Telefone do cliente",
        verbose_name="Telefone"
    )

    email = models.EmailField(
        null=False, blank=False,
        max_length=100,
        validators=[MinLengthValidator(20), MaxLengthValidator(100)],
        help_text="Email do cliente",
        verbose_name="Email"
    )

    ativo = models.BooleanField(
        null=False, blank=False,
        default=True,
        verbose_name="Ativo"
    )


    def __str__(self):
        return self.nome