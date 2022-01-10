from time import sleep
from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_04_a.html"
browser = Firefox()

browser.get(url)
sleep(3)

ul = browser.find_element_by_tag_name('ul')
lista_li = ul.find_elements_by_tag_name('li')
lista[0].find_element_by_tag_name('a').text