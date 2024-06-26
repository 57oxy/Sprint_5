from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants
from confest import driver
from confest import login_test_constructor


class TestStellarBurgersConstructor:

    def test_go_to_sauces(self, login_test_constructor):
        driver = login_test_constructor
        WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.SAUCES_LINK_ACTIVE))).click()
        current = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.SAUCES_LINK_ACTIVE))).get_attribute('class')
        assert current == Constants.SAUCES_LINK_ACTIVE

    def test_go_to_fillings(self, login_test_constructor):
        driver = login_test_constructor
        WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.FILLINGS_LINK_ACTIVE))).click()
        current = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((Locators.FILLINGS_LINK_ACTIVE))).get_attribute('class')
        assert current == Constants.FILLINGS_LINK_ACTIVE

    def test_go_to_breads(self, login_test_constructor):
        driver = login_test_constructor
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.FILLINGS_LINK_ACTIVE))).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.BREADS_LINK_ACTIVE))).click()
        current = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.BREADS_LINK_ACTIVE))).get_attribute('class')
        assert current == Constants.BREADS_LINK_ACTIVE