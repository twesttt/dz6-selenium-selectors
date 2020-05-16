from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import logging
from .common.Navigation import Navigation



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.navigation = Navigation(self.driver)

    """Я случайно попробовала здесь добавить пустой basicConfig, но он каким-то чудом получает нужные параметры!!!"""
    logging.basicConfig()
    logger = logging.getLogger('BasePage')
    logger.warning("I'm on Base Page")

    def __element(self, selector):
        """Возвращает элемент по селектору"""

        by = By.CSS_SELECTOR
        return self.driver.find_element(by, selector)

    def _click(self, selector):
        """Реализует клик по элементу"""
        with allure.step(f"Клик по элементу {selector}"):
            self.__element(selector).click()
            return self

    def _input(self, selector, value):
        """Осуществляет ввод значения в текстовое поле"""
        element = self.__element(selector)
        element.clear()
        with allure.step(f"В поле: {selector} вводим значение: {value}"):
            element.send_keys(value)

    def _wait_for_visible(self, selector, wait=3):
        """Ожидает когда элемент станет видимым"""

        WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector)))
        return self

    def _get_element_text(self, selector):
        """Возвращает текстовое значение у элемента"""
        try:
            return self.__element(selector).text
        except NoSuchElementException:
            "Product is not found"
            return False

    def check_console_logs(self):
        with allure.step("Проверяем наличие ошибок в консоли:"):
            console_logs = self.driver.get_log("browser")
            if len(console_logs) > 0:
                for i in console_logs:
                    print(i)
                logging.warning("THERE ARE ERRORS IN CONSOLE")
