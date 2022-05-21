from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os



try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element_by_id('book')
    button1.click()

    x = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x.text
    x = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element_by_xpath('//*[@id="answer"]')
    answer.send_keys(x)
    sumbit = browser.find_element_by_css_selector('button[type="submit"]')
    sumbit.click()

finally:
    time.sleep(10)
    browser.quit()
