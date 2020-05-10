#!/usr/bin/env python
import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging


def pytest_addoption(parser):
    """Параметр для задания url"""

    # parser.addoption("--url", "-U", action="store", default="http://localhost/opencart", help="Specify opencart url")
    parser.addoption("--url", "-U", action="store", default="https://demo.opencart.com/admin", help="Specify opencart url")
    parser.addoption("--browser", "-B", action="store", default="firefox", help="Select browser")
    parser.addoption("--wait", action="store", default=20, help="Specify browser implicitly wait")
    parser.addoption("--log_file", action="store", default=None, help="Specify file name for the log output")
    parser.addoption("--log_level", action="store", default="warning", help="Define log level")
    parser.addoption("--executor", action="store", default="192.168.0.100")


class MyListener(AbstractEventListener):
    logger = logging.getLogger("Driver")

    def before_navigate_to(self, url, driver):
        self.logger.info(f"I'm navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"I'm on {url}")

    def before_navigate_back(self, driver):
        self.logger.info(f"I'm navigating back")

    def after_navigate_back(self, driver):
        self.logger.info(f"I'm back!")

    def before_find(self, by, value, driver):
        self.logger.info(f"I'm looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        self.logger.info(f"I've found '{value}' with '{by}'")

    def before_execute_script(self, script, driver):
        self.logger.info(f"I'm executing '{script}'")

    def after_execute_script(self, script, driver):
        self.logger.info(f"I've executed '{script}'")

    def before_quit(self, driver):
        self.logger.info(f"I'm getting ready to terminate {driver}")

    def after_quit(self, driver):
        self.logger.info(f"WASTED!!!")

    def on_exception(self, exception, driver):
        logging.error(f'Oooops i got: {exception}')
        driver.save_screenshot(f'{exception}.png')


@pytest.fixture
def browser(request):
    logging.info("----Browser initialization----")
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        desired_capabilities = DesiredCapabilities.CHROME
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        driver = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=desired_capabilities, options=opt),
                                      MyListener())
    elif browser_param == "firefox":
        driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.get(request.config.getoption("--url"))
    wait_param = request.config.getoption("--wait")
    driver.implicitly_wait(wait_param)
    driver.maximize_window()
    logging.info("----End of browser fixture----")
    request.addfinalizer(driver.close)
    return driver


"""Run tests remotely using Selenium Grid"""
@pytest.fixture
def remote(request):
    wait_param = request.config.getoption("--wait")
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    wd = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                          desired_capabilities={"browserName": browser})
    wd.implicitly_wait(wait_param)
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd


"""Run tests in cloud: browserstack.com"""

BROWSERSTACK_URL = 'https://bsuser68289:smCMgosDxjqegxW2Rvfe@hub-cloud.browserstack.com/wd/hub'

desired_cap = {

    'os': 'Windows',
    'os_version': '10',
    'browser': 'Firefox',
    'browser_version': '76.0 beta',
    'name': "Test Demo Opencart Firefox "

}


@pytest.fixture
def cloud(request):
    wait_param = request.config.getoption("--wait")
    url = request.config.getoption("--url")
    wd = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    wd.implicitly_wait(wait_param)
    wd.maximize_window()
    wd.get(url)
    request.addfinalizer(wd.quit)
    return wd
