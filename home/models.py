from django.db import models
import django.utils.timezone


from django.conf.urls.static import static
from django.conf import settings

from datetime import datetime
# Create your models here.

SIMOUNAO = (
    ('S', 'S'),
    ('N', 'N'),
)
CATEGORIAS = (
    ('CELULAR','CELULAR'),('CADERNO','CADERNO'),('CALCULADORA','CALCULADORA'),
)

UNIVERSIDADES = ( ('UNB','UNB'),('CATOLICA','CATOLICA'))


class objeto(models.Model):
    def __str__(self):
        return "Objeto : " + self.nomeObjeto + "  | Status retirado : [" + self.retirado.upper() +"]"
    nomeObjeto = models.CharField(max_length=100)
    localEncontrado = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    categoria = models.CharField(max_length=100,null=True,choices=CATEGORIAS)
    faculdade = models.CharField(max_length=100,choices=UNIVERSIDADES)
    descricao = models.CharField(max_length=500,null=True)
    date = models.DateField(("Date"), default= django.utils.timezone.now)
    retirado = models.CharField(max_length=1,choices=SIMOUNAO)
    nomePessoaRetirado = models.CharField(max_length=100, blank = True)
    identidade = models.CharField(max_length=20, blank = True)
    telefoneContato = models.CharField(max_length=100, blank = True)