from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.support.ui import Select




try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')

    num1 = browser.find_element(By.ID, 'num1')
    one = int(num1.text)

    num2 = browser.find_element(By.ID, "num2")
    two = int(num2.text)

    sum = str(one+two)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum)

    button3 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button3.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()