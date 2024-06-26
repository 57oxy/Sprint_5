from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants

# добавляем модули без них фикстуры не подгружаются
from confest import driver
from confest import login

# Инициализация объекта фейкера
faker = Faker()


class TestStellarBurgersRegiter:

    # Тест проверяющий функционал регистрации
    def test_registration_positive(self, driver):
        # добавление прерывания между командами вебдрайвера
        driver.implicitly_wait(4)

        # Создаем фейковый уникальный имейл для регистрации
        email = faker.email()

        # Жмем кнопку Войти в аккаунт на главной странице
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.SIGN_IN_BUTTON))).click()
        # Переходим по ссылке Зарегистрироваться
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.REGISTER_LINK))).click()
        # Отправляем логин в поле Имя
        driver.find_element(*Locators.REGISTER_LOGIN).send_keys("tester")
        # Отправляем созданный уникальный имейл в поле Email
        driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        # Отправляем пароль из констант в поле Пароль
        driver.find_element(*Locators.REGISTER_PASSWORD).send_keys(Constants.PASSWORD)
        # Нажимаем на кнопку Зарегистрироваться
        driver.find_element(*Locators.AUTH_BUTTON).click()

    # Проверяем регистрацию
    def test_login(self, login):
        # Передаем результаты работы модуля login
        driver = login
        # Получаем содержимое value поля Email
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        # Сравниваем содержимое value поля Email и константу с Email
        assert email == Constants.EMAIL

    # Проверяем ошибку при некорректном пароле
    def test_registration_error_password(self, driver):
        # добавление прерывания между командами вебдрайвера
        driver.implicitly_wait(4)

        # Создаем фейковый уникальный имейл для регистрации
        email = faker.email()

        # Жмем кнопку Войти в аккаунт на главной странице
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.SIGN_IN_BUTTON))).click()
        # Переходим по ссылке Зарегистрироваться
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.REGISTER_LINK))).click()
        # Отправляем логин в поле Имя
        driver.find_element(*Locators.REGISTER_LOGIN).send_keys("tester")
        # Отправляем созданный уникальный имейл в поле Email
        driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        # Отправляем некорректный пароль из констант в поле Пароль
        driver.find_element(*Locators.REGISTER_PASSWORD).send_keys(Constants.INCORRECT_PASSWORD)
        # Жмем кнопку Зарегистрироваться
        driver.find_element(*Locators.AUTH_BUTTON).click()
        # Получаем текст ошибки если она есть
        error = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.REGISTER_PASSWORD_ERROR_MESSAGE))).text
        # Сравниваем текст ошибки с константой которая была скопирована со страницы
        assert error == Constants.INCORRECT_PASSWORD_ERROR_MESSAGE
