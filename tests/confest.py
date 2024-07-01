import pytest
from selenium import webdriver
from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()


# модуль входа в систему с переходом в личный кабинет
@pytest.fixture
def login(driver):
    # нажимаем кнопку Войти в аккаунт на главной странице
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    # передаем имейл из констант
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    # передаем пароль из констант
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    # нажимаем кнопку Войти
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    # нажимаем кнопку Личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    return driver
