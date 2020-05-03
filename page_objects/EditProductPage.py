# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage
import logging


class EditProductPage(BasePage):
    """Локаторы для страницы редактирования продукта"""

    FORM_PRODUCT = "#form-product"
    TAB_GENERAL = "a[href='#tab-general']"
    PRODUCT_NAME = "#input-name1"
    TAB_DATA = "a[href='#tab-data']"
    META_TAG_TITLE = "#input-meta-title1"
    INPUT_PRICE = "#input-price"
    INPUT_QUANTITY = "#input-quantity"
    MODEL_NAME = "#input-model"
    TAB_LINKS = "a[href='#tab-links']"
    TAB_ATTRIBUTE = "a[href='#tab-attribute']"
    TAB_OPTION = "a[href='#tab-option']"
    TAB_RECURRING = "a[href='#tab-recurring']"
    TAB_DISCOUNT = "a[href='#tab-discount']"
    TAB_SPECIAL = "a[href='#tab-special']"
    ADD_SPECIAL = "button[data-original-title='Add Special']"
    LAST_ADDED_SPECIAL = "table[id='special'] tbody tr:nth-last-child(1)"
    LAST_ADDED_SPECIAL = "table[id='special'] tbody tr:nth-last-child(1)"
    DELETE_LAST_ADDED_SPECIAL = "table[id='special'] tbody tr:nth-last-child(1) button[data-original-title='Remove']"
    INPUT_PRIORITY_OF_SPECIAL = "table[id='special'] tbody tr:nth-last-child(1) input[placeholder='Priority']"
    INPUT_PRICE_OF_SPECIAL = "table[id='special'] tbody tr:nth-last-child(1) input[placeholder='Price']"
    TAB_IMAGE = "a[href='#tab-image']"
    SAVE_BUTTON = "button[data-original-title='Save']"

    logger = logging.getLogger('EditProductPage')
    logger.info("I'm on Edit Product Page")

    def fill_the_required_product_fields(self, test_data):
        """Заполняем форму продукта тестовыми данными"""

        self._wait_for_visible(self.FORM_PRODUCT)
        self._input(self.PRODUCT_NAME, test_data)
        self._input(self.META_TAG_TITLE, test_data)
        self._click(self.TAB_DATA)
        self._input(self.MODEL_NAME, test_data)
        self.logger.info("Product form is filled with new data")
        return self

    def change_product_price(self, price):
        """Изменяет цену продукта"""

        self._click(self.TAB_DATA)
        self._input(self.INPUT_PRICE, price)
        self.logger.info(f'Product price is changed to {price}')
        return self

    def change_product_quantity(self, quantity):
        """Изменяет количество продукта"""

        self._click(self.TAB_DATA)
        self._input(self.INPUT_QUANTITY, quantity)
        self.logger.info(f'Product quantity is changed to {quantity}')
        return self

    def add_special(self, priority, price):
        """Добавляет специальную цену продукта"""

        self._click(self.TAB_SPECIAL)
        self._click(self.ADD_SPECIAL)
        self._input(self.INPUT_PRIORITY_OF_SPECIAL, priority)
        self._input(self.INPUT_PRICE_OF_SPECIAL, price)
        return self

    def delete_last_added_special(self):
        """Удалает последнюю добавленную специальную цену продукта"""

        self._click(self.TAB_SPECIAL)
        self._click(self.DELETE_LAST_ADDED_SPECIAL)
        return self

    def save_product_information(self):
        """Сохранить изменения в описании продукта"""

        self._click(self.SAVE_BUTTON)
        self.logger.info("New product information is saved")
        return self
