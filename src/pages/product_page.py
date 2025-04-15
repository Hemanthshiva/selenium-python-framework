import logging

from selenium.webdriver.common.by import By

import src.utils.logger as logger
from src.data.product import Product
from src.pages.header_page import HeaderPage


class ProductPage(HeaderPage):
    log = logger.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    PRODUCT_SEARCH_BOX = (By.NAME, "search")
    SEARCH_PRODUCT_LIST = (By.CSS_SELECTOR, "#entry_217822 ul.dropdown-menu")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-id='216816'] h1")
    PRODUCT_CODE = (By.CSS_SELECTOR, "[data-id='216820'] span:not(.ls-label)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-id='216831'] .price-new")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-id='216842'] [title='Add to Cart']")
    SIZE_SELECT_OPTION = (By.XPATH, "(//select[contains(@name,'option')])[1]")
    QUANTITY_INPUT = (By.NAME, "quantity")

    def search_and_assert_product_details(self, product: Product):
        if isinstance(product, dict):
            product = Product.from_dict(product)  # Convert to Product instance
        elif not isinstance(product, Product):
            raise ValueError("Expected 'product' to be instance of 'Product' or 'dict'.")

        search_box = self.get_element(*self.PRODUCT_SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(product.name)
        self.wait_for_element(*self.SEARCH_PRODUCT_LIST)
        product_list = self.get_element(*self.SEARCH_PRODUCT_LIST)

        if product_list:
            # Locate the first 'li a' element within the found 'li' elements
            first_link = product_list.find_element(By.CSS_SELECTOR, "li .title a:nth-child(1)")
            first_link.click()
        else:
            raise Exception("No products found in the search results")

        # Fetch elements once and reuse values
        title_element = self.get_element(*self.PRODUCT_TITLE)
        code_element = self.get_element(*self.PRODUCT_CODE)
        price_element = self.get_element(*self.PRODUCT_PRICE)

        title = title_element.text
        code = code_element.text
        price = price_element.text

        assert title == product.name, f"Expected product title {product.name}, but got {title}."
        assert code == product.code, f"Expected product code {product.code}, but got {code}."
        assert price == product.price, f"Expected product price {product.price}, but got {price}."

    def add_product_to_cart_and_verify_product_added_to_cart(self, product: Product):
        self.select_last_option_from_dropdown()

        add_to_cart_button = self.wait_for_element_to_be_clickable(*self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

        alert_text = self.handle_alert(retrieve_text=True)
        assert "Success: You have added" in alert_text, \
            f"Expected alert to contain 'Success: You have added', but got {alert_text}."

    def select_last_option_from_dropdown(self):
        try:
            size_select = self.get_element(*self.SIZE_SELECT_OPTION)
            size_select.click()
            all_options = size_select.find_elements(By.TAG_NAME, "option")
            if all_options:
                all_options[-1].click()
            else:
                raise Exception("No size options available to select")
        except Exception as e:
            self.log.error(f"Could not select size: {e}")
