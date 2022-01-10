from time import sleep
from urllib.parse import urlparse

from selenium.webdriver import Firefox


def get_anchors(browser, element):
    """Obtém elementos ancoras aninhados ao elemento web em questão.

    Args:
        browser (selenium.Webdriver): Instância do Navegador.
        element (selenium.WebElement): Elemento Web.

    Returns:
        list : Elementos âncoras
    """
    elemento = browser.find_element_by_tag_name(element)
    list_a = elemento.find_elements_by_tag_name('a')
    return list_a


url = "https://selenium.dunossauro.live/exercicio_03.html"
browser = Firefox()

browser.get(url)

##### Home Page
sleep(5)
list_a = get_anchors(browser, 'main')
list_a[0].click()

##### Page 1
sleep(3)
list_p = browser.find_elements_by_tag_name('p')
list_a = get_anchors(browser, 'main')

number1 = int(list_p[1].text.split()[0])
number2 = int(list_p[1].text.split()[2])
result = number1 * number2

if result == int(list_a[0].text):
    list_a[1].click()
else:
    list_a[0].click()


##### Page 2
sleep(60)
title = browser.title
list_a = get_anchors(browser, 'main')

if title == list_a[0].text:
    list_a[0].click()
else:
    list_a[1].click()


##### Page 3
sleep(3)
path = urlparse(browser.current_url).path.replace('/', '')
list_a = get_anchors(browser, 'main')

if path == list_a[0].text:
    list_a[0].click()
else:
    list_a[1].click()
    

##### Final Page
sleep(3)
browser.refresh()
print("Jogador Venceu!")


# sleep(10)
# browser.quit()
