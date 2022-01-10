from time import sleep
from selenium.webdriver import Firefox


def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto `text`.
    
    Argumentos:
        - browser = Instância do browser.
        - tag = Tag onde o texto será procurado.
        - text = Conteúdo que deve estar na tag.
    """
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento
        

url = "https://selenium.dunossauro.live/aula_04_b.html"
browser = Firefox()

browser.get(url)
sleep(3)

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']
for nome in nome_das_caixas:
    sleep(0.5)
    find_by_text(browser, 'div', nome).click()

for nome in nome_das_caixas:
    sleep(0.5)
    browser.back()

for nome in nome_das_caixas:
    sleep(0.5)
    browser.forward()
