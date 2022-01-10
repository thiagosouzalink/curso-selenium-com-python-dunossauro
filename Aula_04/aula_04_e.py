"""
1. Pegar todos os links de 
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
"""
from time import sleep
from pprint import pprint

from selenium.webdriver import Firefox


def get_links(browser, element):
    """Pega todos os links dentro de um elemento.
    
    Argumentos
        - browser = A instância do navegador.
        - element = Webelement [aside, main, body, ul, ol]
    """
    resultado = {}
    elemento = browser.find_element_by_tag_name(element)
    ancoras = elemento.find_elements_by_tag_name('a')
    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')
    return resultado
    
    
url = "https://selenium.dunossauro.live/aula_04.html"
browser = Firefox()

browser.get(url)
sleep(5)

########## PARTE 01
aulas = get_links(browser, 'aside')
pprint(aulas)


########## PARTE 02
exercicios = get_links(browser, 'main')
pprint(exercicios)

browser.get(exercicios['Exercício 3'])

