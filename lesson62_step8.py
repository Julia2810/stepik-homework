from cgitb import html

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


link = "https://suninjuly.github.io/registration1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div[class='form-group first_class']>input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div[class='first_block']>.form-group second_class>input")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div[class='form-group third_class']>input")
    input3.send_keys("mail@mail.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
/html/body/div/form/div[1]/div[2]/input