from .BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


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
    FIRST_PRODUCT_PRICE = "#form-product > div > table > tbody > tr > td:nth-child(5)"
    FIRST_PRODUCT_SPECIAL_PRICE = "#form-product > div > table > tbody > tr > td:nth-child(5) .text-danger"
    FIRST_PRODUCT_QUANTITY = "#form-product > div > table > tbody > tr > td:nth-child(6)"

    def find_product(self, product_name):
        """Находит продукт из списка по имени и возвращает текст из поля Product Name"""

        self._wait_for_visible(self.FILTER_PRODUCT_FORM)
        self._input(self.INPUT_PRODUCT_NAME_IN_FILTER, product_name)
        self._click(self.FILTER_BUTTON)
        try:
            return self._get_element_text(self.FIRST_PRODUCT_IN_THE_LIST)
        except NoSuchElementException:
            "Product is not found"
            return False

    def click_add_product(self):
        """Добавляет продукт"""

        self._click(AdminProductsPage.ADD_PRODUCT)

    def click_edit_product(self):
        """Изменяет имя продукта"""

        self._click(self.FIRST_PRODUCT_EDIT_BUTTON)

    def delete_product(self, name):
        """Удалаяет продукт"""

        self.find_product(name)
        self._click(self.FIRST_PRODUCT_CHECKBOX)
        self._click(self.DELETE_PRODUCT)
        self.driver.switch_to_alert().accept()

    def get_product_info(self, element):
        """Возвращает текст характеристики продукта"""

        return self._get_element_text(element)
