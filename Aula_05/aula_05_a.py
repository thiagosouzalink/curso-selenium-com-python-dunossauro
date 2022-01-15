from time import sleep

from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_05_a.html"
browser = Firefox()

browser.get(url)
sleep(1)

div_python = browser.find_element_by_id('python')
div_haskell = browser.find_element_by_id('haskell')

print(div_python.text)
print(div_haskell.text)

sleep(7.5)
browser.quit()