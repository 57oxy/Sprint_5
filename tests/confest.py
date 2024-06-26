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
    # добавление прерывания между командами вебдрайвера
    driver.implicitly_wait(6)
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

# модуль входа в систему для тестирования Конструктора без перехода в Личный кабинет
@pytest.fixture
def login_test_constructor(driver):
    # добавление прерывания между командами вебдрайвера
    driver.implicitly_wait(6)
    # нажимаем кнопку Войти в аккаунт на главной странице
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    # передаем имейл из констант
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    # передаем пароль из констант
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    # нажимаем кнопку Войти
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver

# модуль входа в систему через кнопку Личный кабинет
@pytest.fixture
def login_via_lk(driver):
    # добавление прерывания между командами вебдрайвера
    driver.implicitly_wait(5)
    # нажимаем кнопку Личный кабинет на главной странице
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    # передаем имейл из констант
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    # передаем пароль из констант
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    # нажимаем кнопку Войти
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    # нажимаем кнопку Личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    return driver

# модуль входа в систему через форму регистрации
@pytest.fixture
def login_via_reg(driver):
    # добавление прерывания между командами вебдрайвера
    driver.implicitly_wait(5)
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
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    return driver

@pytest.fixture
def login_via_recovery(driver):
    # добавление прерывания между командами вебдрайвера
    driver.implicitly_wait(5)
    # нажимаем кнопку Войти в аккаунт на главной странице
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    # нажимаем кнопку Восстановить пароль
    driver.find_element(*Locators.PASS_RECOVERY_LINK).click()
    # передаем email для восстановления пароля из констант
    driver.find_element(*Locators.PASS_RECOVERY_EMAIL).send_keys(Constants.EMAIL)
    # нажимаем кнопку Восстановить
    driver.find_element(*Locators.PASS_RECOVERY_BUTTON).click()
    return driver