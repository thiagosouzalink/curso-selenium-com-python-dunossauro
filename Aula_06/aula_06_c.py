from time import sleep

from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_06_a.html"
browser = Firefox()

browser.get(url)
sleep(2)

browser.find_elements_by_css_selector('div.form-group')

browser.find_elements_by_css_selector(
    'div.form-group + br' # br irmão de div class form-group
)[1].get_attribute('id')

# da tag div com a classe form-group pegue o filho com id dentro-nome
browser.find_element_by_css_selector('div.form-group > #dentro-nome')
browser.find_element_by_css_selector('div.form-group > #dentro-nome')

# do form, pegue todas as tag label existentes
# ignorando a hierarquia (decendente)
browser.find_elements_by_css_selector('form label')

# https://flukeout.github.io