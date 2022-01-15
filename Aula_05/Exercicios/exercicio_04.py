import json
from time import sleep
from urllib.parse import urlparse
from xml.dom.minidom import Element

from selenium.webdriver import Firefox


def fill_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


url = "https://selenium.dunossauro.live/exercicio_04.html"
browser = Firefox()

browser.get(url)
sleep(5)

data = {'nome': 'Thiago',
         'email': 'thiago@mail.com',
         'senha': 'q1w2e3r4',
         'telefone': '999999999'}

fill_form(browser, **data)

sleep(3)
# Create dictionary from query string text
query = urlparse(browser.current_url).query.replace('%40', '@')
dict_query = {key: value 
              for key, value in (element.split('=') 
                                 for element in query.split('&')[:-1])
            }

# Create dictionary from textarea text
ta_text = browser.find_element_by_tag_name('textarea').text.replace("'", "\"")
dict_ta_text = json.loads(ta_text)

assert dict_query == dict_ta_text
print("url e resultados são iguais.")

# sleep(10)
# browser.quit()