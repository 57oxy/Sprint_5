from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Переход на страницу регистрации
driver.get("https://stellarburgers.nomoreparties.site/register")

# Ожидание загрузки страницы
time.sleep(5)

# Определение локаторов
# Ввод данных в поле для ввода имени
driver.find_element(By.XPATH, "//label[contains(text(), 'Имя')]/..//input").send_keys("tester")

# Ввод данных в поле для ввода email
driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/..//input").send_keys("test_testov_1_1@domain.ru")

# Ввод данных в поле для ввода пароля
driver.find_element(By.XPATH, "//label[contains(text(), 'Пароль')]/..//input").send_keys("passw0rd")

# Нажатие на кнопку регистрации
driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()

# Ожидание загрузки страницы после регистрации
time.sleep(5)

# Закрытие браузера
driver.quit()