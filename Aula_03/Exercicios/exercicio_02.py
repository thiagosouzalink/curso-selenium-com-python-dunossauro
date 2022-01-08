from time import sleep

from selenium.webdriver import Firefox


url = "https://curso-python-selenium.netlify.app/exercicio_02.html"
browser = Firefox()

browser.get(url)
sleep(5)

while True:
    a = browser.find_element_by_tag_name('a')
    sleep(1)
    a.click()
    
    list_p = browser.find_elements_by_tag_name('p')
    expected_number = list_p[1].text.split(':')[1].strip()
    p = list_p[-1].text
    
    if expected_number in p:
        break
    
# sleep(15)
# browser.quit()