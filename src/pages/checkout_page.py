import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import src.utils.logger as logger
from src.pages.header_page import HeaderPage


class CheckoutPage(HeaderPage):
    log = logger.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    GUEST_CHECKOUT_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='input-account-guest']")
    FIRSTNAME_INPUT = (By.NAME, "firstname")
    LASTNAME_INPUT = (By.NAME, "lastname")
    EMAIL_INPUT = (By.NAME, "email")
    TELEPHONE_INPUT = (By.NAME, "telephone")
    ADDRESS1_INPUT = (By.NAME, "address_1")
    CITY_INPUT = (By.NAME, "city")
    POSTCODE_INPUT = (By.NAME, "postcode")
    COUNTRY_DROPDOWN = (By.NAME, "country_id")
    REGION_DROPDOWN = (By.NAME, "zone_id")
    COMMENT_INPUT = (By.NAME, "comment")
    TsANDCs_CHECKBOX = (By.CSS_SELECTOR, "label[for='input-agree']")
    CONTINUE_BUTTON = (By.ID, "button-save")

    def checkout_as_a_guest(self, user):
        self.get_element(*self.GUEST_CHECKOUT_RADIO_BUTTON).click()
        self.get_element(*self.FIRSTNAME_INPUT).send_keys(user.first_name)
        self.get_element(*self.LASTNAME_INPUT).send_keys(user.last_name)
        self.get_element(*self.EMAIL_INPUT).send_keys(user.email)
        self.get_element(*self.TELEPHONE_INPUT).send_keys(user.phone_number)
        self.get_element(*self.ADDRESS1_INPUT).send_keys(user.address.line1)
        self.get_element(*self.CITY_INPUT).send_keys(user.address.city)
        self.get_element(*self.POSTCODE_INPUT).send_keys(user.address.postcode)
        country_dropdown = Select(self.get_element(*self.COUNTRY_DROPDOWN))
        country_dropdown.select_by_visible_text(user.address.country)

        region_dropdown = Select(self.get_element(*self.REGION_DROPDOWN))
        region_dropdown.select_by_visible_text(user.address.region)
        self.get_element(*self.COMMENT_INPUT).send_keys("Test comment")
        self.get_element(*self.TsANDCs_CHECKBOX).click()
        self.get_element(*self.CONTINUE_BUTTON).click()
