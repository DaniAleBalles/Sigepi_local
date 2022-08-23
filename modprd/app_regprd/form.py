# App de registro de un producto - Formulario para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 23 -08-2022

from django import forms
from django.forms import ModelForm
from django import forms
from .models import *
from modprd.app_regprd.models import *

class form_prd(forms.ModelForm):
    class Meta:
        model = prd_base
        fields = (
            'nombre_prd',
            'fech_entrega',
            'id_pry',
            'id_us',
        )
        labels ={
            'nombre_prd': 'Nombre del producto',
            'fech_entrega': 'Fecha de entrega estimada',
            'id_pry': 'Proyecto de referencia',
            'id_us': 'Propietario del producto',
        }

class form_prd(forms.ModelForm):
    class Meta:
        model = prd_base
        fields = (
            'nombre_prd',
            'fech_reg',
            'id_pry',
            'id_us',
        )
        labels ={
            'nombre_prd': 'Nombre del producto',
            'fech_reg': 'Fecha de registro del producto',
            'id_pry': 'Proyecto de referencia',
            'id_us': 'Propietario del producto',
        }

class form_reg_prd(forms.ModelForm):
    class Meta:
        model = prd_base
        fields = (
            'nombre_prd',
            'fech_entrega',
            'id_pry',
            'id_us',
        )
        labels ={
            'nombre_prd': 'Nombre del producto',
            'fech_entrega': 'Fecha de entrega estimada',
            'id_pry': 'Proyecto de referencia',
            'id_us': 'Propietario del producto',
        }
