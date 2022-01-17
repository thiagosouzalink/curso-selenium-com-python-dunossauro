from time import sleep

from selenium.webdriver import Firefox


def fill_form(form):
    """Preencher o formulário de modo automatizado.

    Args:
        form (str): Nome do formulário a ser buscado.
    """
    browser.find_element_by_css_selector(
        f'.form-{form} input[type="text"]').send_keys('Robô')
    browser.find_element_by_css_selector(
        f'.form-{form} input[type="password"]').send_keys('12345')
    browser.find_element_by_css_selector(
        f'.form-{form} input[type="submit"]').click()


url = "https://selenium.dunossauro.live/exercicio_05.html"
browser = Firefox()

browser.get(url)

while True:
    sleep(2)
    word_form = browser.find_element_by_css_selector('header span').text
    if "terminar" in word_form:
        break
    fill_form(word_form)

print("Os formulários foram todos preenchidos de forma automatizada.")

# sleep(10)
# browser.quit()