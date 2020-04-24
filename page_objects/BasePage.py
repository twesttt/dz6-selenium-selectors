from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .common.Navigation import Navigation


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.navigation = Navigation(self.driver)

    def __element(self, selector):
        by = By.CSS_SELECTOR
        return self.driver.find_element(by, selector)

    def _click(self, selector):
        ActionChains(self.driver).move_to_element(self.__element(selector)).click().perform()

    def _input(self, selector, value):
        element = self.__element(selector)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector)))

    # def _wait_for_element_presence(self, element_locator, wait):
    #     return WebDriverWait(self.driver, wait).\
    #         until(EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))

    def _get_element_text(self, selector):
        return self.__element(selector).text