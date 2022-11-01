# Lista de urls para las vistas del desarrollo de producto - URL's para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 30 -10 -2022

from django.urls import path
from .models import *
from modprd.app_desprd.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    #Url's Para el registro de producto

    path('mis_productos/', login_required(vst_list_des.as_view()), name='listar_etp'), # urlpara la consulta de productos

]