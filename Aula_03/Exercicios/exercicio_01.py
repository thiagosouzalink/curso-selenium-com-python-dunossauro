from time import sleep
from pprint import pprint

from selenium.webdriver import Firefox


url = "https://curso-python-selenium.netlify.app/exercicio_01.html"
browser = Firefox()

browser.get(url)
sleep(5)

h1 = browser.find_element_by_tag_name('h1')
list_p = browser.find_elements_by_tag_name('p')

dictionary = {f'{h1.text}': {}}
for i in range(len(list_p)):
    dictionary[h1.text][list_p[i].get_attribute('atributo')] = list_p[i].text

pprint(dictionary)

# sleep(10)
# browser.quit()