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
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)
    
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium провер€ть в течение 12 секунд, пока кнопка не станет кликабельной
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
    # ожидание чтобы визуально оценить результаты прохождени€ скрипта
    time.sleep(10)
    # закрываем браузер после всех манипул€ций
    browser.quit()

# не забываем оставить пустую строку в конце файла
