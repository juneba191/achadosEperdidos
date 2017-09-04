from django.db import models
import django.utils.timezone


from django.conf.urls.static import static
from django.conf import settings

from datetime import datetime
# Create your models here.

class objeto(models.Model):
    def __str__(self):
        return "Objeto : " + self.nomeObjeto + "  | Status retirado : [" + self.retirado.upper() +"]"
    nomeObjeto = models.CharField(max_length=100)
    localEncontrado = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    categoria = models.CharField(max_length=100,null=True)
    faculdade = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500,null=True)
    date = models.DateField(("Date"), default= django.utils.timezone.now)
    retirado = models.CharField(max_length=1)
    nomePessoaRetirado = models.CharField(max_length=100,null=True)
    identidade = models.CharField(max_length=20,null=True)
    telefoneContato = models.CharField(max_length=100,null=True)





