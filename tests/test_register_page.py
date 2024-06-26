from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants
from confest import driver
from confest import login


faker = Faker()


class TestStellarBurgersRegiter:

    def test_registration_positive(self, driver):
        driver.implicitly_wait(4)
        email = faker.email()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.SIGN_IN_BUTTON))).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.REGISTER_LINK))).click()
        driver.find_element(*Locators.REGISTER_LOGIN).send_keys("tester")
        driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.REGISTER_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5)

    def test_login(self, login):
        driver = login
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        assert email == Constants.EMAIL

    def test_registration_error_password(self, driver):
        driver.implicitly_wait(4)
        email = faker.email()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.SIGN_IN_BUTTON))).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.REGISTER_LINK))).click()
        driver.find_element(*Locators.REGISTER_LOGIN).send_keys("tester")
        driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.REGISTER_PASSWORD).send_keys(Constants.INCORRECT_PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        error = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.REGISTER_PASSWORD_ERROR_MESSAGE))).text
        assert error == Constants.INCORRECT_PASSWORD_ERROR_MESSAGE
