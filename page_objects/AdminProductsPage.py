from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage


class AdminProductsPage(BasePage):

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

    # def __init__(self, driver):
    #     self.driver = driver

    def find_product(self, product_name):
        """Находит продукт из списка по имени и возвращает текст из поля Product Name"""
        # br = self.driver
        self._wait_for_visible(self.FILTER_PRODUCT_FORM)
        self._input(self.INPUT_PRODUCT_NAME_IN_FILTER, product_name)
        # input_product_name = br.find_element(By.CSS_SELECTOR,
        #                                      self.INPUT_PRODUCT_NAME_IN_FILTER)
        # input_product_name.clear()
        # input_product_name.send_keys(product_name)
        self._click(self.FILTER_BUTTON)
        # br.find_element(By.CSS_SELECTOR, self.FILTER_BUTTON).click()
        try:
            # found_product = br.find_element(By.CSS_SELECTOR,
            #                                 )
            # return found_product.text
            return self._get_element_text(self.FIRST_PRODUCT_IN_THE_LIST)
        except NoSuchElementException:
            "Product is not found"
            return False

    def click_add_product(self):
        """Добавляет продукт"""
        br = self.driver
        # br.find_element(By.CSS_SELECTOR, AdminProductsPage.ADD_PRODUCT).click()
        self._click(AdminProductsPage.ADD_PRODUCT)

    def click_edit_product(self):
        """Изменяет имя продукта"""
        # br = self.driver
        # edit_product_button = br.find_element(By.CSS_SELECTOR,
        #                                       self.FIRST_PRODUCT_EDIT_BUTTON)
        # edit_product_button.click()
        self._click(self.FIRST_PRODUCT_EDIT_BUTTON)

    def delete_product(self, name):
        """Удалаяет продукт"""

        br = self.driver
        self.find_product(name)
        product_checkbox = br.find_element(By.CSS_SELECTOR,
                                           self.FIRST_PRODUCT_CHECKBOX)
        product_checkbox.click()
        br.find_element(By.CSS_SELECTOR,
                        self.DELETE_PRODUCT).click()
        alert = br.switch_to_alert()
        alert.accept()
