# -*- coding: utf-8 -*-
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

def sobre(request):
    template = loader.get_template('sobre.html')

    context = {

    }
    return HttpResponse(template.render(context,request))

def item(request, item_id):
    print("id do item %s" % item_id)
    item = objeto.objects.get(pk=item_id)
    template = loader.get_template('item.html')
    context = {
        'objetos': item
    }
    return HttpResponse(template.render(context,request))

def busca(request, nome):

    lista_objetos  = objeto.objects.filter(nomeObjeto__startswith=nome)
    template = loader.get_template('busca.html')
    context = {
        'objetos' : lista_objetos
    }
    return HttpResponse(template.render(context,request))
