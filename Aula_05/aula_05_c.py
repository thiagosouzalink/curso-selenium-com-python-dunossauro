from time import sleep

from selenium.webdriver import Firefox


url = "https://selenium.dunossauro.live/aula_05_c.html"
browser = Firefox()

browser.get(url)
sleep(1)

def melhor_filme(browser, filme, email, telefone):
    """Preenche o formulário do melhor filme de 2020."""
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click

# browser.find_element_by_name('filme').send_keys('Parasita')
# email = browser.find_element_by_name('email')
# email.send_keys('thiago@mail.com')
# telefone = browser.find_element_by_name('telefone')
# telefone.send_keys('(091)999999999')
# browser.find_element_by_name('enviar').click()

melhor_filme(browser, 'Parasita', 'thiago@mail.com', '(091)999999999')


sleep(7.5)
browser.quit()