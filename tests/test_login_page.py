from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants

# добавляем модули без них фикстуры не подгружаются
from confest import driver
from confest import login
from confest import login_via_lk
from confest import login_via_reg
from confest import login_via_recovery


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
    def test_login_via_personal_account_button(self, login_via_lk):
        # Передаем результаты работы модуля login_via_lk - фикстуру из confest с помощью которой производится вход
        driver = login_via_lk
        # Получаем текст атрибута value поля Email
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        # Сравниваем содержимое value поля Email и константу с Email
        assert email == Constants.EMAIL

    # Тестируем вход через форму регистрации
    def test_login_via_registration_form(self, login_via_reg):
        # Передаем результаты работы модуля login_via_reg - фикстуру из confest с помощью которой производится вход
        driver = login_via_reg
        # Получаем текст атрибута value поля Email
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        # Сравниваем содержимое value поля Email и константу с Email
        assert email == Constants.EMAIL

    # Тестируем вход восстановление пароля
    def test_login_via_recovery_form(self, login_via_recovery):
        # Передаем результаты работы модуля login_via_recovery - фикстуру из confest с помощью которой производится вход
        driver = login_via_recovery
        # Получаем текст атрибута label он должен содержать значение Восстановление пароля
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASS_RECOVERY_PAGE_LABEL))).text
        # Сравниваем содержимое label и константу с необходимым текстом
        assert label == Constants.PASS_RECOVERY_PAGE_LABEL
