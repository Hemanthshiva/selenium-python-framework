import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def page(browser, env):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser option: chrome or firefox")
    parser.addoption("--env", action="store", default="dev", help="environment option: dev or prod")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")
