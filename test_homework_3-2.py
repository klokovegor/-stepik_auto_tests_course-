from selenium import webdriver
import time
import unittest



class TestCase(unittest.TestCase):
    def test_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys('Illness')
        input2 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys('Illness')
        input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys('Illness')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_second(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys('Illness')
        input2 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys('Illness')
        input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys('Illness')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()



if __name__ == "__main__":
    unittest.main()