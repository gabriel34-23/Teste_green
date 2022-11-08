from django.contrib import admin
from .models import Cidade, Banco, CreditoRural, TipoLicenca, LicencaAmbiental


admin.site.register(Cidade)
admin.site.register(Banco)
admin.site.register(CreditoRural)
admin.site.register(TipoLicenca)
admin.site.register(LicencaAmbiental)