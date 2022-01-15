from time import sleep
from urllib.parse import urlparse
from json import loads

from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_05.html"
browser = Firefox()

browser.get(url)
sleep(12)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


estrutura = {'nome': 'Thiago',
             'email': 'thiago@mail.com',
             'senha': 'q1w2e3r4',
             'telefone': '999999999'}

preenche_form(browser, **estrutura)
url_parse = urlparse(browser.current_url)

sleep(5)
texto_resultado = browser.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace("\'", "\"")

dict_result = loads(resultado_arrumado)

assert dict_result == estrutura
# sleep(7.5)
# browser.quit()