from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button1 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CLASS_NAME, 'form-control')
    input1.send_keys(y)

    button3 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button3.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()