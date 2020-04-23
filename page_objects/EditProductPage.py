from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EditProductPage:
    """Локаторы для страницы редактирования продукта"""

    FORM_PRODUCT = "#form-product"
    TAB_GENERAL = "a[href='#tab-general']"
    PRODUCT_NAME = "#input-name1"
    TAB_DATA = "a[href='#tab-data']"
    META_TAG_TITLE = "#input-meta-title1"
    MODEL_NAME = "#input-model"
    TAB_LINKS = "a[href='#tab-links']"
    TAB_ATTRIBUTE = "a[href='#tab-attribute']"
    TAB_OPTION = "a[href='#tab-option']"
    TAB_RECURRING = "a[href='#tab-recurring']"
    TAB_DISCOUNT = "a[href='#tab-discount']"
    TAB_SPECIAL = "a[href='#tab-special']"
    TAB_IMAGE = "a[href='#tab-image']"
    SAVE_BUTTON = "button[data-original-title='Save']"

    def __init__(self, driver):
        self.driver = driver

    def _wait_for_element_presence(self, element_locator, wait):
        return WebDriverWait(self.driver, wait). \
            until(EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))

    def fill_the_product_form_with_test_data(self, test_data):
        """Заполняем форму продукта тестовыми данными"""

        br = self.driver
        self._wait_for_element_presence(self.FORM_PRODUCT, 10)
        product_name = br.find_element(By.CSS_SELECTOR, self.PRODUCT_NAME)
        product_name.clear()
        product_name.send_keys(test_data)
        meta_tag = br.find_element(By.CSS_SELECTOR, self.META_TAG_TITLE)
        meta_tag.send_keys(test_data)
        br.find_element(By.CSS_SELECTOR, self.TAB_DATA).click()
        model_name = br.find_element(By.CSS_SELECTOR, self.MODEL_NAME)
        model_name.send_keys(test_data)

    def save_product_information(self):
        """Сохранить изменения в описании продукта"""

        br = self.driver
        save_button = br.find_element(By.CSS_SELECTOR,
                                      self.SAVE_BUTTON)
        save_button.click()
