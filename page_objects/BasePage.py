from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .common.Navigation import Navigation


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.navigation = Navigation(self.driver)

    def __element(self, selector):
        """Возвращает элемент по селектору"""

        by = By.CSS_SELECTOR
        return self.driver.find_element(by, selector)

    def _click(self, selector):
        """Реализует клик по элементу"""

        ActionChains(self.driver).move_to_element(self.__element(selector)).click().perform()

    def _input(self, selector, value):
        """Осуществляет ввод значения в текстовое поле"""

        element = self.__element(selector)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, wait=3):
        """Ожидает когда элемент станет видимым"""

        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector)))

    def _get_element_text(self, selector):
        """Возвращает текстовое значение у элемента"""
        try:
            return self.__element(selector).text
        except NoSuchElementException:
            "Product is not found"
            return False
