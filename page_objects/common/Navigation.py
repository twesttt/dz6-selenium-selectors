from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Navigation:

    def __init__(self, driver):
        self.driver = driver

    """Локаторы для панели навигации в админке"""

    NAVIGATION_PANEL = "#navigation"
    MENU_CATALOG = "#menu-catalog > a"
    CATEGORIES_LIST = "#collapse1 > li:nth-child(1) > a"
    PRODUCTS_LIST = "#collapse1 > li:nth-child(2) > a"

    def expand_catalog(self):
        br = self.driver
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.MENU_CATALOG)))
        br.find_element(By.CSS_SELECTOR, self.MENU_CATALOG).click()
        print("Expand catalog")
        return self

    def open_products_page(self):
        br = self.driver
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.PRODUCTS_LIST)))
        print("Open product page")
        br.find_element(By.CSS_SELECTOR, self.PRODUCTS_LIST).click()
        return self
