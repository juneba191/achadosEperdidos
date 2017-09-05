from django.contrib import admin
from .models import objeto
from django import forms
# Register your models here.


#admin.site.register(objeto)

admin.site.site_header= "Achados e Perdidos UnB"
admin.site.site_title = "achados e perdidos."
admin.site.index_title = "Achados e Perdidos"


#escrever o selector de opcoes.

class SelectSimOuNao(forms.ModelChoiceField):
    Escolhas = (
        ('S', 'SIM'),
        ('N','NAO'),
    )
    stuff = forms.ChoiceField(choices=Escolhas)


# define as opções de busca do modelo objeto
@admin.register(objeto)
class Objeto(admin.ModelAdmin):
    date_hierarchy = 'date'
    search_fields = ['nomeObjeto']
    list_display = ['nomeObjeto','categoria','faculdade']
    list_filter =('categoria','faculdade','localEncontrado')
    retirado = SelectSimOuNao
