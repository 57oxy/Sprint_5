from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants
from confest import driver
from confest import login


class TestStellarBurgersPersonalAccount:

    def test_go_to_personal_account_page(self, login):
        driver = login
        email = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        assert email == Constants.EMAIL

    def test_go_to_constructor(self, login):
        driver = login
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.CONSTRUCTOR_LINK))).click()
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.CONSTRUCTOR_LABEL))).text
        assert label == Constants.CONSTRUCTOR_LABEL

    def test_go_to_logo(self, login):
        driver = login
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.CONSTRUCTOR_LINK))).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.LOGO_LINK))).click()
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.CONSTRUCTOR_LABEL))).text
        assert label == Constants.CONSTRUCTOR_LABEL

    def test_log_out(self, login):
        driver = login
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.LOG_OUT_BUTTON))).click()
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.LOG_OUT_LABEL))).text
        assert label == Constants.LOG_OUT_LABEL