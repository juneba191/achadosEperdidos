from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    url(r'^sobre',views.sobre,name='sobre'),
    url(r'^',views.index,name='index'),

]
