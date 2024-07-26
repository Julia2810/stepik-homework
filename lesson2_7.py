from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os




try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/file_input.html')

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.ru")

    with open("test.txt", "w") as file:
        content = file.write("automationbypython")

    input4 = browser.find_element(By.NAME, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)


    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()