import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import src.utils.logger as logger


class BasePage:
    log = logger.custom_logger(logging.DEBUG)
    ALERT = (By.CSS_SELECTOR, "[role='alert']")
    ALERT_TEXT = (By.CSS_SELECTOR, ".toast-body p")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url: str):
        self.log.info(f"Navigating to \"{url}\"")
        self.driver.get(url)

    def get_element(self, by, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        self.log.info(f"Get element by: \"{by}\", and value: \"{value}\"")
        return self.driver.find_element(by, value)

    def get_multiple(self, by, value):
        lf.log.info(f"Get elements by: \"{by}\", and value: \"{value}\"")
        return self.driver.find_elements(by, value)

    def hover_over(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        self.log.info(f"Hover over an element")

    def wait_for_element_to_be_clickable(self, by: By, value: str):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((by, value))
            )
        except TimeoutException:
            self.log.error(f"Element located by {by} with value {value} was not clickable after 10 seconds")
            raise

    def wait_for_element(self, by, value):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((by, value)))
            self.log.info(f"Element located by: \"{by}\", with value: \"{value}\"")
            return True
        except TimeoutException:
            self.log.error(f"Could not find element by: \"{by}\", with value: \"{value}\"")
            return False

    def assert_alert_present(self, timeout=10):
        """Asserts that an alert is present within the given timeout."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            self.log.info("Alert is present")
            return True
        except TimeoutException:
            self.log.error("No alert found within the time frame")
            return False

    def handle_alert(self, retrieve_text=False):
        try:
            if not self.get_element(*self.ALERT):
                self.log.info("No alert present.")
                return None if retrieve_text else False

            alert_text = self.get_element(*self.ALERT_TEXT).text
            if alert_text is None:
                self.log.error("Alert text is None")
                return ""

            self.log.info(f"Alert text retrieved: {alert_text}")
            return alert_text
        except TimeoutException:
            self.log.error("No alert found within the time frame")
            return None if retrieve_text else False
        except UnhandledAlertException as e:
            self.log.error(f"Unhandled alert exception: {e}")
            return None if retrieve_text else False

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.log.info(f"Scrolled into view: {element}")
