# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest

def doTheWork(browser, link):
    browser.get(link)
    input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
    input1.send_keys("cowabunga")
    input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
    input2.send_keys("cowabunga")
    input3 = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
    input3.send_keys("cowabunga")
    # Îòïðàâëÿåì çàïîëíåííóþ ôîðìó
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Ïðîâåðÿåì, ÷òî ñìîãëè çàðåãèñòðèðîâàòüñÿ
    # æäåì çàãðóçêè ñòðàíèöû
    time.sleep(3)
    # íàõîäèì ýëåìåíò, ñîäåðæàùèé òåêñò
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # çàïèñûâàåì â ïåðåìåííóþ welcome_text òåêñò èç ýëåìåíòà welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text

class TestLink(unittest.TestCase):
    def setUp(self):
        self.textToCheck = 'Congratulations! You have successfully registered!'
        self.browser = webdriver.Chrome()
        self.errorMessage = 'Something wrong'
    def tearDown(self):
        self.browser.quit()
        time.sleep(5)
    def test_first_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        input1.send_keys("cowabunga")
        input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
        input2.send_keys("cowabunga")
        input3 = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        input3.send_keys("cowabunga")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(self.textToCheck, welcome_text, self.errorMessage)
    def test_second_link(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        input1.send_keys("cowabunga")
        input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
        input2.send_keys("cowabunga")
        input3 = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        input3.send_keys("cowabunga")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(self.textToCheck, welcome_text, self.errorMessage)

if __name__ == "__main__":
    unittest.main()
    time.sleep(5)

