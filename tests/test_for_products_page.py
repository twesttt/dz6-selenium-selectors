#!/usr/bin/env python

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from page_objects import AdminLoginPage, AdminProductsPage, EditProductPage, AdminHomePage
import time


def test_add_product(browser):
    """Проверяет воркфлоу добавления продукта с тестовым именем "test_name", после удаляет его"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")

    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
    #                                            AdminMainPage.NAVIGATION_PANEL)))
    AdminHomePage(browser).navigation.expand_catalog()
    AdminHomePage(browser).navigation.open_products_page()
    AdminProductsPage(browser).click_add_product()
    EditProductPage(browser).fill_the_product_form_with_test_data("test_name")
    EditProductPage(browser).save_product_information()
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
    #                                            AdminProductsPage.FILTER_PRODUCT_FORM)))

    found_product_name = AdminProductsPage(browser).find_product("test_name")
    assert found_product_name == "test_name"
    AdminProductsPage(browser).delete_product("test_name")


def test_edit_product(browser):
    """Проверяет редактирование продукта (изменяется его имя)"""

    br = browser
    wait = WebDriverWait(br, 10)
    AdminLoginPage(br).admin_login("admin", "admin")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminMainPage.NAVIGATION_PANEL)))
    AdminMainPage(br).expand_catalog()
    AdminMainPage(br).open_catalog_page(AdminMainPage.PRODUCTS_LIST)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsPage.FILTER_PRODUCT_FORM)))
    AdminProductsPage(br).find_product("iPhone")
    product_checkbox = br.find_element(By.CSS_SELECTOR,
                                       AdminProductsPage.FIRST_PRODUCT_CHECKBOX)
    product_checkbox.click()
    AdminProductsPage(br).click_edit_product()
    EditProductPage(br).fill_the_product_form_with_test_data("Edited iPhone")
    EditProductPage(br).save_product_information()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsPage.FILTER_PRODUCT_FORM)))
    AdminProductsPage(br).find_product("Edited iPhone")
    product_checkbox = br.find_element(By.CSS_SELECTOR,
                                       AdminProductsPage.FIRST_PRODUCT_CHECKBOX)
    product_checkbox.click()
    AdminProductsPage(br).click_edit_product()
    EditProductPage(br).fill_the_product_form_with_test_data("iPhone")
    EditProductPage(br).save_product_information()


def test_delete_product(browser):
    """Проверяет удаление продукта"""

    br = browser
    br.maximize_window()
    wait = WebDriverWait(br, 10)
    AdminLoginPage(br).admin_login("admin", "admin")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminMainPage.NAVIGATION_PANEL)))
    AdminMainPage(br).expand_catalog()
    AdminMainPage(br).open_catalog_page(AdminMainPage.PRODUCTS_LIST)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               AdminProductsPage.ADD_PRODUCT)))
    AdminProductsPage(br).click_add_product()
    EditProductPage(br).fill_the_product_form_with_test_data("test_name")
    EditProductPage(br).save_product_information()
    AdminProductsPage(br).delete_product("test_name")
    found_product = AdminProductsPage(br).find_product("test_name")
    assert found_product is False
