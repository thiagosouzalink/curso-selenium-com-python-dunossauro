from time import sleep
from selenium.webdriver import Firefox


url = "https://curso-python-selenium.netlify.app/aula_03.html"
browser = Firefox()

browser.get(url)

sleep(5)
a = browser.find_element_by_tag_name('a')

for click in range(10):
    list_p = browser.find_elements_by_tag_name('p')
    a.click()
    print(f"Valor de p: {list_p[-1].text} , valor do click: {click}", end=' ')
    print(f"- Os valores são iguais: {int(list_p[-1].text)==click}")

sleep(5)
browser.quit()