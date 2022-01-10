from time import sleep
from urllib.parse import urlparse

from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_04_b.html"
browser = Firefox()

browser.get(url)
sleep(3)

url_parseada = urlparse(browser.current_url)

