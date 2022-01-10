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
        
        
def find_by_href(browser, link):
    """Encontrar o elemento `a` com o link `link`.
    
    Argumentos:
        - browser = Instância do browser.
        - link = Link que será procurado.
    """
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento
    

url = "https://selenium.dunossauro.live/aula_04_a.html"
browser = Firefox()

browser.get(url)
sleep(3)

elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
elemento_ddg_link = find_by_href(browser, 'ddg')
