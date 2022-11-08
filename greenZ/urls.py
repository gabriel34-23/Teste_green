from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_cidade', views.add_cidade, name= 'add_cidade'),
    path('cidade_list', views.cidade_list, name= 'cidade_list'),
    path('add_banco', views.add_banco, name= 'add_banco'),
    path('banco_list', views.banco_list, name= 'banco_list'),
    path('add_tipoLicenca', views.add_tipoLicenca , name= 'add_tipoLicenca'),
    path('tipoLicenca_list', views.tipoLicenca_list, name= 'tipoLicenca_list'),
    path('add_creditoRural', views.add_creditoRural, name= 'add_creditoRural'),
    path('credito_list', views.credito_list, name= 'credito_list'),
    path('add_licencaAmbiental', views.add_licencaAmbiental, name= 'add_licencaAmbiental'),
    path('licenca_list', views.licenca_list, name= 'licenca_list'),
]