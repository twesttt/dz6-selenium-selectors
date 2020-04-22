from selenium.webdriver.common.by import By


class AdminMainPage:

    def __init__(self, driver):
        self.driver = driver

    """Локаторы для панели навигации в админке"""

    NAVIGATION_PANEL = "#navigation"
    MENU_CATALOG = "#menu-catalog > a"
    CATEGORIES_LIST = "#collapse1 > li:nth-child(1) > a"
    PRODUCTS_LIST = "#collapse1 > li:nth-child(2) > a"

    def expand_catalog(self):
        br = self.driver
        br.find_element(By.CSS_SELECTOR, self.MENU_CATALOG).click()

    def open_catalog_page(self, page_locator):
        br = self.driver
        br.find_element(By.CSS_SELECTOR, page_locator).click()


