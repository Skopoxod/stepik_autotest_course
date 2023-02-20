# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    #input3 = browser.find_element(By.CLASS_NAME, "form-control city")
    #input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # óñïåâàåì ñêîïèðîâàòü êîä çà 30 ñåêóíä
    time.sleep(30)
    # çàêðûâàåì áðàóçåð ïîñëå âñåõ ìàíèïóëÿöèé
    browser.quit()

# íå çàáûâàåì îñòàâèòü ïóñòóþ ñòðîêó â êîíöå ôàéëà
