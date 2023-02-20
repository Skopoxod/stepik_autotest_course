# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    # ãîâîðèì WebDriver æäàòü âñå ýëåìåíòû â òå÷åíèå 5 ñåêóíä
    browser.implicitly_wait(5)
    
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # ãîâîðèì Selenium ïðîâåðÿòü â òå÷åíèå 12 ñåêóíä, ïîêà êíîïêà íå ñòàíåò êëèêàáåëüíîé
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x_element.text)
    
    _input = browser.find_element(By.CSS_SELECTOR, "#answer")
    _input.send_keys(y)
    
    button = browser.find_element(By.ID, "solve")
    button.click()
    
    #assert "successful" in message.text

finally:
    # îæèäàíèå ÷òîáû âèçóàëüíî îöåíèòü ðåçóëüòàòû ïðîõîæäåíèÿ ñêðèïòà
    time.sleep(10)
    # çàêðûâàåì áðàóçåð ïîñëå âñåõ ìàíèïóëÿöèé
    browser.quit()

# íå çàáûâàåì îñòàâèòü ïóñòóþ ñòðîêó â êîíöå ôàéëà
