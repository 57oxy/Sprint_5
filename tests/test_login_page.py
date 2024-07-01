from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants

# добавляем модули без них фикстуры не подгружаются
from confest import driver
from confest import login


class TestStellarBurgersLogin:

    # Тестируем вход через главную страницу
    def test_login_via_homepage(self, login):
        # Передаем результаты работы модуля login
        driver = login
        # Получаем текст атрибута value поля Email
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        # Сравниваем содержимое value поля Email и константу с Email
        assert email == Constants.EMAIL

    # Тестируем вход через кнопку Личный кабинет
    def test_login_via_personal_account_button(self, driver):
        # нажимаем кнопку Личный кабинет на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        # передаем имейл из констант
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        # передаем пароль из констант
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        # нажимаем кнопку Войти
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        # нажимаем кнопку Личный кабинет
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_BUTTON))).click()
        # Получаем текст атрибута value поля Email
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        # Сравниваем содержимое value поля Email и константу с Email
        assert email == Constants.EMAIL

    # Тестируем вход через форму регистрации
    def test_login_via_registration_form(self, driver):
        # нажимаем кнопку Войти в аккаунт на главной странице
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        # нажимаем кнопку Зарегистрироваться
        driver.find_element(*Locators.REGISTER_LINK).click()
        # нажимаем кнопку Войти
        driver.find_element(*Locators.LOGIN_LINK).click()
        # передаем имейл из констант
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        # передаем пароль из констант
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        # нажимаем кнопку Войти
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        # нажимаем кнопку Личный кабинет
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_BUTTON))).click()
        # Получаем текст атрибута value поля Email
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        # Сравниваем содержимое value поля Email и константу с Email
        assert email == Constants.EMAIL

    # Тестируем вход восстановление пароля
    def test_login_via_recovery_form(self, driver):
        # нажимаем кнопку Войти в аккаунт на главной странице
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        # нажимаем кнопку Восстановить пароль
        driver.find_element(*Locators.PASS_RECOVERY_LINK).click()
        # передаем email для восстановления пароля из констант
        driver.find_element(*Locators.PASS_RECOVERY_EMAIL).send_keys(Constants.EMAIL)
        # нажимаем кнопку Восстановить
        driver.find_element(*Locators.PASS_RECOVERY_BUTTON).click()
        # Получаем текст атрибута label он должен содержать значение Восстановление пароля
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASS_RECOVERY_PAGE_LABEL))).text
        # Сравниваем содержимое label и константу с необходимым текстом
        assert label == Constants.PASS_RECOVERY_PAGE_LABEL
