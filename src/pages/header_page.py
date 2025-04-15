import logging

from selenium.webdriver.common.by import By

import src.utils.logger as logger
from src.pages.base_page import BasePage


class HeaderPage(BasePage):
    log = logger.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    HEADER_CART_LINK = (By.CSS_SELECTOR, "[data-id='217825'] a")
    HEADER_CART_CONTAINER = (By.ID, "cart-total-drawer")
    CART_CONTAINER_EDIT_CART_BUTTON = (By.CSS_SELECTOR, "[id='entry_217850'] a")
    MY_ACCOUNT_MENU_ITEM = (By.XPATH, "//div[@id='widget-navbar-217834']//span[contains(text(),'My account')]")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    LOGIN_FORM = (By.CSS_SELECTOR, "form [value='Login']")

    def navigate_to_login_page(self):
        # Fetch the 'My Account' menu item
        my_account = self.get_element(*self.MY_ACCOUNT_MENU_ITEM)
        self.hover_over(my_account)

        # Fetch and click the 'Login' link
        login = self.get_element(*self.LOGIN_LINK)
        login.click()

        # Wait for the login form to appear and assert its presence
        assert self.wait_for_element(*self.LOGIN_FORM) is True

    def navigate_to_shopping_cart(self):
        self.get_element(*self.HEADER_CART_LINK).click()
        cart_container = self.wait_for_element(*self.HEADER_CART_CONTAINER)
        if cart_container:
            self.get_element(*self.CART_CONTAINER_EDIT_CART_BUTTON).click()
        else:
            self.log.error("Unable to navigate to cart")
            raise AssertionError("Cart container not found, unable to navigate to cart")
