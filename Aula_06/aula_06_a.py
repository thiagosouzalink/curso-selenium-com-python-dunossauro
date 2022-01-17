from time import sleep

from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_06_a.html"
browser = Firefox()

browser.get(url)
sleep(2)

browser.find_element_by_css_selector('input').send_keys('Thiago')