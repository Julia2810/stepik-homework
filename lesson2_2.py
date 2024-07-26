from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    picture = browser.find_element(By.ID, 'treasure')
    picture_checked = picture.get_attribute("valuex")

    x_element = picture_checked
    x = x_element
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()

    button2 = browser.find_element(By.ID, "robotsRule")
    button2.click()

    button3 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()