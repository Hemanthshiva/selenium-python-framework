import logging

from selenium.webdriver.common.by import By

import src.utils.logger as logger
from src.data.product import Product
from src.pages.header_page import HeaderPage


class ShoppingCartPage(HeaderPage):
    log = logger.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    SHOPPING_CART_CONTAINER = (By.ID, "checkout-cart")
    PRODUCT_CONTAINER_TABLE = (By.CSS_SELECTOR, "#checkout-cart tbody:nth-child(2)")
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")

    def assert_product_details_on_shopping_cart(self, product: Product):
        if isinstance(product, dict):
            product = Product.from_dict(product)
        elif not isinstance(product, Product):
            raise ValueError("Expected 'product' to be instance of 'Product' or 'dict'.")
        shopping_cart_container = self.wait_for_element(*self.SHOPPING_CART_CONTAINER)
        assert shopping_cart_container is not None, f"Unable to land on shopping cart page"
        product_table = self.get_element(*self.PRODUCT_CONTAINER_TABLE)
        product_rows = product_table.find_elements(By.TAG_NAME, "tr")
        product_count = len(product_rows)
        # Add assertion for expected product count.  Example:
        assert product_count == 1, f"Expected 1 product in cart, but found {product_count}"

        product_details_list = []

        for product_index, product_row in enumerate(product_rows, start=1):
            product_name = product_row.find_element(By.CSS_SELECTOR, f"td:nth-child(2) a").text
            product_code = product_row.find_element(By.CSS_SELECTOR, f"td:nth-child(3)").text
            product_price = product_row.find_element(By.CSS_SELECTOR, f"td:nth-child(5)").text

            product_details_list.append({
                "name": product_name,
                "code": product_code,
                "price": product_price
            })

        print(f"Product details: {product_details_list}")

        for product_detail in product_details_list:
            assert product.name == product_detail[
                "name"], f"Expected product name {product.name}, but got {product_detail['name']}."
            assert product.code == product_detail[
                "code"], f"Expected product code {product.code}, but got {product_detail['code']}."
            assert product.price == product_detail[
                "price"], f"Expected product price {product.price}, but got {product_detail['price']}."

    def continue_to_checkout(self):
        self.get_element(*self.CHECKOUT_BUTTON).click()
