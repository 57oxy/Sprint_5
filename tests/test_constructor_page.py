from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants

# добавляем модули без них фикстуры не подгружаются
from confest import driver
from confest import login_test_constructor


class TestStellarBurgersConstructor:

    # Проверяем Переход в Соусы
    def test_go_to_sauces(self, login_test_constructor):
        # Передаем результаты работы модуля login_test_constructor
        driver = login_test_constructor
        # Переходим по ссылке Соусы
        WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.SAUCES_LINK_ACTIVE))).click()
        # Получаем текст атрибута class ссылки Соусы
        current = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.SAUCES_LINK_ACTIVE))).get_attribute('class')
        # Сравниваем атрибута class и константу с необходимым текстом класса
        assert current == Constants.SAUCES_LINK_ACTIVE

    # Проверяем Переход в Начинки
    def test_go_to_fillings(self, login_test_constructor):
        # Передаем результаты работы модуля login_test_constructor
        driver = login_test_constructor
        # Переходим по ссылке Начинки
        WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.FILLINGS_LINK_ACTIVE))).click()
        # Получаем текст атрибута class ссылки Начинки
        current = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.FILLINGS_LINK_ACTIVE))).get_attribute('class')
        # Сравниваем атрибута class и константу с необходимым текстом класса
        assert current == Constants.FILLINGS_LINK_ACTIVE

    # Проверяем Переход обратно в Булки
    def test_go_to_breads(self, login_test_constructor):
        # Передаем результаты работы модуля login_test_constructor
        driver = login_test_constructor
        # Переходим по ссылке Начинки
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.FILLINGS_LINK_ACTIVE))).click()
        # Переходим по ссылке Булки
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.BREADS_LINK_ACTIVE))).click()
        # Получаем текст атрибута class ссылки Булки
        current = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.BREADS_LINK_ACTIVE))).get_attribute('class')
        # Сравниваем атрибута class и константу с необходимым текстом класса
        assert current == Constants.BREADS_LINK_ACTIVE