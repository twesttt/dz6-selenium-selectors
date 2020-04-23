from .BasePage import BasePage


class AdminHomePage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    """НЕВЕРНЫЕ ЛОКАТОРЫ - ПЕРЕПИСАТЬ !!!!!"""

    USERNAME = "#input-username"
    PASSWORD = "#input-password"
    FORGOTTEN_PASSWORD = "span.help-block a"
    LOGIN = "button[type='submit']"
    OPEN_CART = "#footer a"