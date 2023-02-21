# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    _window2 = browser.window_handles[1]
    browser.switch_to.window(_window2)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x_element.text)
    
    _input = browser.find_element(By.CSS_SELECTOR, "#answer")
    _input.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

    # Ïðîâåðÿåì, ÷òî ñìîãëè çàðåãèñòðèðîâàòüñÿ
    # æäåì çàãðóçêè ñòðàíèöû
    time.sleep(5)


finally:
    # îæèäàíèå ÷òîáû âèçóàëüíî îöåíèòü ðåçóëüòàòû ïðîõîæäåíèÿ ñêðèïòà
    time.sleep(10)
    # çàêðûâàåì áðàóçåð ïîñëå âñåõ ìàíèïóëÿöèé
    browser.quit()

# íå çàáûâàåì îñòàâèòü ïóñòóþ ñòðîêó â êîíöå ôàéëà
