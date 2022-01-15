from time import sleep

from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_05_b.html"
browser = Firefox()

browser.get(url)
sleep(1)

topico = browser.find_element_by_class_name('topico')
linguagens = browser.find_elements_by_class_name('linguagens')

for linguagem in linguagens:
    print((linguagem.find_element_by_tag_name('h2').text,
           linguagem.find_element_by_tag_name('p').text))

sleep(7.5)
browser.quit()
