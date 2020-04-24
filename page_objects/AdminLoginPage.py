from .BasePage import BasePage


class AdminLoginPage(BasePage):
    """Локаторы на странице логина для администратора"""

    USERNAME = "#input-username"
    PASSWORD = "#input-password"
    FORGOTTEN_PASSWORD = "span.help-block a"
    LOGIN = "button[type='submit']"
    OPEN_CART = "#footer a"

    def admin_login(self, username, password):
        """Логин под админом"""

        self.driver.get("http://localhost/opencart/admin/")
        self._input(self.USERNAME, username)
        self._input(self.PASSWORD, password)
        self._click(self.LOGIN)
        return self
