# Sistema de Achados e Perdidos ( trabalho de engenharia de software )

# Dependências.

1 - Django ( para instalar, rode pip3 install django )

2 - Python3

3 - Mysqli ? (Sendo decidido ainda)


# Material de Apoio.

1 - Documentação Django

  https://docs.djangoproject.com/en/1.11/
 
2 - Tutorais Youtube.

  https://www.youtube.com/watch?v=Ky59C5geOtg&list=PLGLfVvz_LVvSMqZiTTsAC7C8Ypp81Jt6D
 
3 - Como fazer funcionar o imageView .


https://stackoverflow.com/questions/15158337/django-admin-link-to-image-via-imagefield


no template utilizar.```<td> <img src="{{MEDIA_URL }}{{ objeto.image.url }}"> </img> </td> ```




https://medium.com/django-musings/customizing-the-django-admin-site-b82c7d325510

https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#adminsite-objects



# Como fazer funcionar abaixo.



# Para criar a base de dados necessária:

    ./manage.py makemigrations
    python manage.py migrate

para criar um usuário administrador para você, va até a

pasta base ( a que possui o 'manage.py') , rode:

    ./manage.py createsuperuser


Após subir o server com ./manage.py runserver
acessa-la no link


    localhost:8000/home
menu administrador


    localhost:8000/admin
    
    
  busca:
  
  
    localhost:8000/busca/(string a ser buscada)
    
    
  busca por id :
  
  
    localhost:8000/item/(id a ser buscado)
    
    
  sobre:
  
    localhost:8000/sobre
   



