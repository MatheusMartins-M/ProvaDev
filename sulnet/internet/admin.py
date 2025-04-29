from django.contrib import admin
from internet.models import Assinatura, Cliente

admin.site.register((Assinatura, Cliente))