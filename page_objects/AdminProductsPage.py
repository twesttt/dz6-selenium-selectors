from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AdminProductsPage:

    def __init__(self, driver):
        self.driver = driver

    """Локаторы для страницы администрирования продуктов"""

    ADD_PRODUCT = "a[data-original-title='Add New']"
    COPY_PRODUCT = "button[data-original-title='Copy']"
    DELETE_PRODUCT = "button[data-original-title='Delete']"
    FILTER_PRODUCT_FORM = "div > #filter-product "
    INPUT_PRODUCT_NAME_IN_FILTER = "div > #filter-product  #input-name"
    FILTER_BUTTON = "div > #filter-product  #button-filter"
    FIRST_PRODUCT_IN_THE_LIST = "#form-product > div > table > tbody > tr > td:nth-child(3)"
    FIRST_PRODUCT_CHECKBOX = "#form-product > div > table > tbody > tr > td:nth-child(1) >\
        input[type=checkbox]"
    FIRST_PRODUCT_EDIT_BUTTON = "#form-product > div > table > tbody > tr > td:nth-child(8)\
        > a > i"

    def find_product(self, product_name):
        """Находит продукт из списка по имени и возвращает текст из поля Product Name"""
        br = self.driver
        input_product_name = br.find_element(By.CSS_SELECTOR,
                                             self.INPUT_PRODUCT_NAME_IN_FILTER)
        input_product_name.clear()
        input_product_name.send_keys(product_name)
        br.find_element(By.CSS_SELECTOR, self.FILTER_BUTTON).click()
        try:
            found_product = br.find_element(By.CSS_SELECTOR,
                                            self.FIRST_PRODUCT_IN_THE_LIST)
            return found_product.text
        except NoSuchElementException:
            "Product is not found"
            return None
