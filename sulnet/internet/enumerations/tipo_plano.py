from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoPlano(models.TextChoices):
    BASIC = "BSC", _("Básico")
    STANDARD = "PDR", _("Padrão")
    PREMIUM = "PRM", _("Premium")
    MASTER = "MSR", _("Master")