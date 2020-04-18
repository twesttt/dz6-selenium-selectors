#!/usr/bin/env python
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Параметр для задания url"""

    parser.addoption("--url", "-U", action="store", default="http://localhost/opencart", help="Specify opencart url")
    parser.addoption("--browser", "-B", action="store", default="chrome", help="Select browser")
    parser.addoption("--wait", action="store", default=20, help="Specify browser implicitly wait")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")
    wait_param = request.config.getoption("--wait")
    driver.implicitly_wait(wait_param)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))

    return driver


