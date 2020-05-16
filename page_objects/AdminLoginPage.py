from .BasePage import BasePage
import logging
import allure

class AdminLoginPage(BasePage):
    """Локаторы на странице логина для администратора"""

    USERNAME = "#input-username"
    PASSWORD = "#input-password"
    FORGOTTEN_PASSWORD = "span.help-block a"
    LOGIN = "button[type='submit']"
    OPEN_CART = "#footer a"

    logger = logging.getLogger('AdminLoginPage')
    logger.info("I am on Admin Login Page")

    def admin_login(self, username, password):
        """Логин под админом"""
        with allure.step(f"Логинимся под:{username}"):
            self._wait_for_visible(self.USERNAME)
            self._input(self.USERNAME, username)
            self._input(self.PASSWORD, password)
            self._click(self.LOGIN)
            self.logger.info(f"I've logged in under '{username}'")
            return self
