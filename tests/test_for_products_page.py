#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdminLoginPage, AdminNavigation, AdminProductsList, EditProduct


def admin_login(br):
    """Логин под админом"""

    br.get("http://localhost/opencart/admin/")
    login = br.find_element(By.CSS_SELECTOR, AdminLoginPage.USERNAME)
    login.send_keys("admin")
    password = br.find_element(By.CSS_SELECTOR, AdminLoginPage.PASSWORD)
    password.send_keys("admin")
    br.find_element(By.CSS_SELECTOR, AdminLoginPage.LOGIN).click()


def open_products_page(br):
    """Открываем страница Products List в админке"""

    br.find_element(By.CSS_SELECTOR, AdminNavigation.MENU_CATALOG).click()
    br.find_element(By.CSS_SELECTOR, AdminNavigation.PRODUCTS_LIST).click()


def fill_the_products_form_with_test_data(br):
    """Заполняем форму продукта тестовыми данными"""

    product_name = br.find_element(By.CSS_SELECTOR, EditProduct.PRODUCT_NAME)
    product_name.send_keys("test_name")
    meta_tag = br.find_element(By.CSS_SELECTOR, EditProduct.META_TAG_TITLE)
    meta_tag.send_keys("test")
    br.find_element(By.CSS_SELECTOR, EditProduct.TAB_DATA).click()
    model_name = br.find_element(By.CSS_SELECTOR, EditProduct.MODEL_NAME)
    model_name.send_keys("test_model")


def edit_product_name(br, name):
    """Изменяет имя продукта"""

    edit_product_button = br.find_element(By.CSS_SELECTOR,
                                          AdminProductsList.FIRST_PRODUCT_EDIT_BUTTON)
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


def delete_product(br, name):
    """Удалаяет продукт"""

    find_product(br, name)
    product_checkbox = br.find_element(By.CSS_SELECTOR,
                                       AdminProductsList.FIRST_PRODUCT_CHECKBOX)
    product_checkbox.click()
    br.find_element(By.CSS_SELECTOR,
                    AdminProductsList.DELETE_PRODUCT).click()
    alert = br.switch_to_alert()
    alert.accept()


def find_product(br, product_name):
    """Находит продукт из списка по имени и возвращает текст из поля Product Name"""

    input_product_name = br.find_element(By.CSS_SELECTOR,
                                         AdminProductsList.PRODUCT_NAME_IN_FILTER)
    input_product_name.clear()
    input_product_name.send_keys(product_name)
    br.find_element(By.CSS_SELECTOR, AdminProductsList.FILTER_BUTTON).click()
    found_product = br.find_element(By.CSS_SELECTOR,
                                    AdminProductsList.FIRST_PRODUCT_IN_THE_LIST)
    return found_product.text


def test_add_product(browser):
    """Проверяет воркфлоу добавления продукта с тестовым именем "test_name", после удаляет его"""

    br = browser
    br.maximize_window()
    wait = WebDriverWait(br, 10)
    admin_login(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminNavigation.NAVIGATION_PANEL)))
    open_products_page(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsList.ADD_PRODUCT)))
    br.find_element(By.CSS_SELECTOR, AdminProductsList.ADD_PRODUCT).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               EditProduct.FORM_PRODUCT)))
    fill_the_products_form_with_test_data(br)
    save_product_information(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsList.FILTER_PRODUCT_FORM)))
    found_product_name = find_product(br, "test_name")
    assert found_product_name == "test_name"
    delete_product(br, "test_name")


def test_edit_product(browser):
    """Проверяет редактирование продукта (изменяется его имя)"""

    br = browser
    br.maximize_window()
    wait = WebDriverWait(br, 10)
    admin_login(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminNavigation.NAVIGATION_PANEL)))
    open_products_page(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsList.FILTER_PRODUCT_FORM)))
    find_product(br, "iPhone")
    product_checkbox = br.find_element(By.CSS_SELECTOR,
                                       AdminProductsList.FIRST_PRODUCT_CHECKBOX)
    product_checkbox.click()
    edit_product_name(br, "Edited iPhone")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsList.FILTER_PRODUCT_FORM)))
    find_product(br, "Edited iPhone")
    product_checkbox = br.find_element(By.CSS_SELECTOR,
                                       AdminProductsList.FIRST_PRODUCT_CHECKBOX)
    product_checkbox.click()
    edit_product_name(br, "iPhone")
