from selenium.webdriver.common.by import By


class AdminLoginPage:

    def __init__(self, driver):
        self.driver = driver

    """Локаторы на странице логина для администратора"""

    USERNAME = "#input-username"
    PASSWORD = "#input-password"
    FORGOTTEN_PASSWORD = "span.help-block a"
    LOGIN = "button[type='submit']"
    OPEN_CART = "#footer a"

    def admin_login(self, username, password):
        """Логин под админом"""
        br = self.driver
        br.get("http://localhost/opencart/admin/")
        login = br.find_element(By.CSS_SELECTOR, AdminLoginPage.USERNAME)
        login.send_keys(username)
        password_input = br.find_element(By.CSS_SELECTOR, AdminLoginPage.PASSWORD)
        password_input.send_keys(password)
        br.find_element(By.CSS_SELECTOR, AdminLoginPage.LOGIN).click()