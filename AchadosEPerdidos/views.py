from django.shortcuts import render
from django.http import  HttpResponse
from .models import objeto
from django.template import loader

def index(request):
    lista_objetos = objeto.objects.all()
    template = loader.get_template('home.html')
    context = {
        'objetos' : lista_objetos
    }
    if lista_objetos is not None:
        print(lista_objetos)
    return HttpResponse(template.render(context,request) )
