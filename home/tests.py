from django.test import TestCase

# Create your tests here.

from selenium import webdriver




print('Iniciando teste de navegação pela página')
driver = webdriver.Firefox()



# Abre a página
driver.get('http://127.0.0.1:8000/')
driver.find_element_by_partial_link_text('clique').click()

