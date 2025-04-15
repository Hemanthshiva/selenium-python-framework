import json
import logging
import os

import pytest
from dotenv import load_dotenv

import src.utils.logger as logger
from src.pages.header_page import HeaderPage
from src.pages.product_page import ProductPage
from src.pages.shopping_cart_page import ShoppingCartPage

load_dotenv()
base_url = os.getenv('BASE_URL')
email_address = os.getenv('EMAIL_ADDRESS')  # Unused variable
password = os.getenv('PASSWORD')  # Unused variable


@pytest.fixture(scope="module")
def product_data():
    with open('src/data/product.json', 'r') as file:
        return json.load(file)


@pytest.fixture
def pages(page, product_data):
    header = HeaderPage(page)
    product_page = ProductPage(page)
    shopping_cart = ShoppingCartPage(page)
    return header, product_page, shopping_cart


@pytest.mark.order(3)
def test_add_product_to_cart(page, pages, product_data):
    log = logger.custom_logger(logging.DEBUG)
    header, product_page, shopping_cart = pages
    product = product_data[1]

    log.info("Starting add to cart test")
    header.navigate_to(base_url)
    log.info("Verifying product details")
    product_page.search_and_assert_product_details(product)
    product_page.add_product_to_cart_and_verify_product_added_to_cart(product)
    product_page.navigate_to_shopping_cart()
    shopping_cart.assert_product_details_on_shopping_cart(product)
