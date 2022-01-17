from time import sleep

from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_06_a.html"
browser = Firefox()

browser.get(url)
sleep(2)

# # [attr=valor] => Deve ser exatamente igual
# ## Usando o atributo type, [attr=valor]
# nome = browser.find_element_by_css_selector('[type="text"]')
# senha = browser.find_element_by_css_selector('[type="password"]')
# btn = browser.find_element_by_css_selector('[type="submit"]')

# ## Usando o atributo name
# nome = browser.find_element_by_css_selector('[name="nome"]')
# senha = browser.find_element_by_css_selector('[name="senha"]')
# btn = browser.find_element_by_css_selector('[name="l0c0"]')


# # [attr*=valor] => Deve ocorrer em
# ## Usando o atributo name
# nome = browser.find_element_by_css_selector('[name*="ome"]')
# senha = browser.find_element_by_css_selector('[name*="nha"]')
# btn = browser.find_element_by_css_selector('[name*="l0"]')


# # [attr|=valor] => Deve ser exatamente igual ou iniciar
# ## Usando o atributo name
# nome = browser.find_element_by_css_selector('[name*="nome"]')
# senha = browser.find_element_by_css_selector('[name*="senha"]')
# btn = browser.find_element_by_css_selector('[name*="l0c0"]')


# [attr^=valor] => Iniciado em
## Usando o atributo name
nome = browser.find_element_by_css_selector('[name*="n"]')
senha = browser.find_element_by_css_selector('[name*="s"]')
btn = browser.find_element_by_css_selector('[name*="l"]')


nome.send_keys('Thiago')
senha.send_keys('batatinha123')
# btn.click()