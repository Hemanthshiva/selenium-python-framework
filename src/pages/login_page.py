import logging

from selenium.webdriver.common.by import By

import src.utils.logger as logger
from src.pages.header_page import HeaderPage


class LoginPage(HeaderPage):
    log = logger.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    EMAIL_ADDRESS = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    MY_ACCOUNT_DASHBOARD = (By.ID, "content")

    def login_with_valid_credentials(self, email_address, password):
        """Login to the application using the provided credentials.
        
        Args:
            email_address: The user's email address
            password: The user's password
        """
        self.log.info(f"Attempting to login with email: {email_address}")
        
        # Clear and fill email field
        email_field = self.get_element(*self.EMAIL_ADDRESS)
        email_field.clear()
        email_field.send_keys(email_address)
        
        # Clear and fill password field
        password_field = self.get_element(*self.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        
        # Click login button
        login_button = self.get_element(*self.LOGIN_BUTTON)
        login_button.click()
        
        # Wait for the dashboard to appear after login
        assert self.wait_for_element(*self.MY_ACCOUNT_DASHBOARD) is True, "Login failed - Dashboard not loaded"
        self.log.info("Login successful")
