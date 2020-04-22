#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import EditProduct
from page_objects import AdminLoginPage, AdminMainPage, AdminProductsPage


def open_products_page(br):
    AdminMainPage(br).expand_catalog()
    AdminMainPage(br).open_catalog_page(AdminMainPage.PRODUCTS_LIST)


def fill_the_products_form_with_test_data(br, test_data):
    """Заполняем форму продукта тестовыми данными"""

    product_name = br.find_element(By.CSS_SELECTOR, EditProduct.PRODUCT_NAME)
    product_name.send_keys(test_data)
    meta_tag = br.find_element(By.CSS_SELECTOR, EditProduct.META_TAG_TITLE)
    meta_tag.send_keys(test_data)
    br.find_element(By.CSS_SELECTOR, EditProduct.TAB_DATA).click()
    model_name = br.find_element(By.CSS_SELECTOR, EditProduct.MODEL_NAME)
    model_name.send_keys(test_data)


def edit_product_name(br, name):
    """Изменяет имя продукта"""

    edit_product_button = br.find_element(By.CSS_SELECTOR,
                                          AdminProductsPage.FIRST_PRODUCT_EDIT_BUTTON)
    edit_product_button.click()
    product_name = br.find_element(By.CSS_SELECTOR,
                                   EditProduct.PRODUCT_NAME)
    product_name.clear()
    product_name.send_keys(name)
    save_product_information(br)


def save_product_information(br):
    """Сохранить изменения в описании продукта"""

    save_button = br.find_element(By.CSS_SELECTOR,
                                  EditProduct.SAVE_BUTTON)
    save_button.click()


def add_product(br, product_name):
    """Добавляет продукт"""

    wait = WebDriverWait(br, 10)
    br.find_element(By.CSS_SELECTOR, AdminProductsPage.ADD_PRODUCT).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               EditProduct.FORM_PRODUCT)))
    fill_the_products_form_with_test_data(br, product_name)
    save_product_information(br)


def delete_product(br, name):
    """Удалаяет продукт"""

    AdminProductsPage(br).find_product(name)
    product_checkbox = br.find_element(By.CSS_SELECTOR,
                                       AdminProductsPage.FIRST_PRODUCT_CHECKBOX)
    product_checkbox.click()
    br.find_element(By.CSS_SELECTOR,
                    AdminProductsPage.DELETE_PRODUCT).click()
    alert = br.switch_to_alert()
    alert.accept()


def test_add_product(browser):
    """Проверяет воркфлоу добавления продукта с тестовым именем "test_name", после удаляет его"""

    br = browser
    br.maximize_window()
    wait = WebDriverWait(br, 10)
    AdminLoginPage(br).admin_login("admin", "admin")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminMainPage.NAVIGATION_PANEL)))
    open_products_page(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsPage.ADD_PRODUCT)))
    add_product(br, "test_name")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsPage.FILTER_PRODUCT_FORM)))
    found_product_name = AdminProductsPage(br).find_product("test_name")
    assert found_product_name == "test_name"
    delete_product(br, "test_name")


def test_edit_product(browser):
    """Проверяет редактирование продукта (изменяется его имя)"""

    br = browser
    br.maximize_window()
    wait = WebDriverWait(br, 10)
    AdminLoginPage(br).admin_login("admin", "admin")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminMainPage.NAVIGATION_PANEL)))
    open_products_page(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsPage.FILTER_PRODUCT_FORM)))
    AdminProductsPage(br).find_product("iPhone")
    # find_product(br, "iPhone")
    product_checkbox = br.find_element(By.CSS_SELECTOR,
                                       AdminProductsPage.FIRST_PRODUCT_CHECKBOX)
    product_checkbox.click()
    edit_product_name(br, "Edited iPhone")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsPage.FILTER_PRODUCT_FORM)))
    AdminProductsPage(br).find_product("Edited iPhone")
    # find_product(br, "Edited iPhone")
    product_checkbox = br.find_element(By.CSS_SELECTOR,
                                       AdminProductsPage.FIRST_PRODUCT_CHECKBOX)
    product_checkbox.click()
    edit_product_name(br, "iPhone")


def test_delete_product(browser):
    """Проверяет удаление продукта"""

    br = browser
    br.maximize_window()
    wait = WebDriverWait(br, 10)
    AdminLoginPage(br).admin_login("admin", "admin")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminMainPage.NAVIGATION_PANEL)))
    open_products_page(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsList.ADD_PRODUCT)))
    add_product(br, "test_name")
    delete_product(br, "test_name")
    found_product = AdminProductsPage(br).find_product("test_name")
    assert found_product is None
