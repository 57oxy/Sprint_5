from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from constants import Constants
from confest import driver
from confest import login
from confest import login_via_lk
from confest import login_via_reg
from confest import login_via_recovery


class TestStellarBurgersLogin:

    def test_login_via_homepage(self, login):
        driver = login
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        assert email == Constants.EMAIL

    def test_login_via_personal_account_button(self, login_via_lk):
        driver = login_via_lk
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        assert email == Constants.EMAIL

    def test_login_via_registration_form(self, login_via_reg):
        driver = login_via_reg
        email = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_EMAIL))).get_attribute("value")
        assert email == Constants.EMAIL

    def test_login_via_recovery_form(self, login_via_recovery):
        driver = login_via_recovery
        label = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASS_RECOVERY_PAGE_LABEL))).text
        assert label == Constants.PASS_RECOVERY_PAGE_LABEL
