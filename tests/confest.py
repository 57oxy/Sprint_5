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


@pytest.fixture
def login(driver):
    driver.implicitly_wait(6)
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    return driver

@pytest.fixture
def login_test_constructor(driver):
    driver.implicitly_wait(6)
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver

@pytest.fixture
def login_via_lk(driver):
    driver.implicitly_wait(5)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    return driver

@pytest.fixture
def login_via_reg(driver):
    driver.implicitly_wait(5)
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.REGISTER_LINK).click()
    driver.find_element(*Locators.LOGIN_LINK).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    return driver

@pytest.fixture
def login_via_recovery(driver):
    driver.implicitly_wait(5)
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.PASS_RECOVERY_LINK).click()
    driver.find_element(*Locators.PASS_RECOVERY_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASS_RECOVERY_BUTTON).click()
    return driver