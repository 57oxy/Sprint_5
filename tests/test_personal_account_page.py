from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants

# добавляем модули без них фикстуры не подгружаются
from confest import driver
from confest import login


class TestStellarBurgersPersonalAccount:

    # Тестируем переход в Личный кабинет
    def test_go_to_personal_account_page(self, login):
        # Передаем результаты работы модуля login
        driver = login
        # Получаем текст атрибута value поля Email
        email = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        # Сравниваем содержимое value поля Email и константу с Email
        assert email == Constants.EMAIL

    # Тестируем переход из Личного кабинета в Конструктор по кнопке Конструктор
    def test_go_to_constructor(self, login):
        # Передаем результаты работы модуля login
        driver = login
        # Переходим в Конструктор по кнопке Конструктор
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.CONSTRUCTOR_LINK))).click()
        # Получаем текст атрибута label он должен содержать значение Соберите бургер
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.CONSTRUCTOR_LABEL))).text
        # Сравниваем содержимое label и константу с необходимым текстом
        assert label == Constants.CONSTRUCTOR_LABEL

    # Тестируем переход из Личного кабинета в Конструктор по кнопке Логотипа
    def test_go_to_logo(self, login):
        # Передаем результаты работы модуля login
        driver = login
        # Переходим в Конструктор по кнопке Конструктор
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.LOGO_LINK))).click()
        # Получаем текст атрибута label он должен содержать значение Соберите бургер
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.CONSTRUCTOR_LABEL))).text
        # Сравниваем содержимое label и константу с необходимым текстом
        assert label == Constants.CONSTRUCTOR_LABEL

    # Тестируем выход из аккаунта
    def test_log_out(self, login):
        # Передаем результаты работы модуля login
        driver = login
        # Нажимаем на кнопку Выйти на странице Личный Кабинет
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.LOG_OUT_BUTTON))).click()
        # Получаем текст атрибута label он должен содержать значение Вход
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.LOG_OUT_LABEL))).text
        # Сравниваем содержимое label и константу с необходимым текстом
        assert label == Constants.LOG_OUT_LABEL