import logging
import os

import pytest
from dotenv import load_dotenv

import src.utils.logger as logger
from src.pages.header_page import HeaderPage
from src.pages.login_page import LoginPage

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv('BASE_URL')


@pytest.fixture(scope="session")
def email_address():
    return os.getenv('EMAIL_ADDRESS')


@pytest.fixture(scope="session")
def password():
    return os.getenv('PASSWORD')


@pytest.fixture(scope="module")
def log():
    return logger.custom_logger(logging.DEBUG)


@pytest.fixture
def header(page):
    return HeaderPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.mark.order(2)
def test_login_form_validation(page, header, login_page, base_url, email_address, password, log):
    log.info("Starting login_form_validation test")

    log.info("Navigating to home page")
    header.navigate_to(base_url)

    log.info("Navigating to login page")
    header.navigate_to_login_page()

    log.info("Loging into the application with valid credentials")
    login_page.login_with_valid_credentials(email_address, password)
