#!/usr/bin/env python
from page_objects import AdminLoginPage, AdminProductsPage, EditProductPage, AdminHomePage


def test_add_product(browser):
    """Проверяет воркфлоу добавления продукта с тестовым именем "test_name", после удаляет его"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation.expand_catalog()
    AdminHomePage(browser).navigation.open_products_page()
    AdminProductsPage(browser).click_add_product()
    EditProductPage(browser).fill_the_product_form_with_test_data("test_name")
    EditProductPage(browser).save_product_information()
    assert AdminProductsPage(browser).find_product("test_name") == "test_name"
    AdminProductsPage(browser).delete_product("test_name")


def test_edit_product(browser):
    """Проверяет редактирование продукта (изменяется его имя)"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation.expand_catalog()
    AdminHomePage(browser).navigation.open_products_page()
    AdminProductsPage(browser)._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM)
    AdminProductsPage(browser).find_product("iPhone")
    AdminProductsPage(browser)._click(AdminProductsPage.FILTER_PRODUCT_FORM)
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser).fill_the_product_form_with_test_data("Edited iPhone")
    EditProductPage(browser).save_product_information()
    AdminProductsPage(browser).find_product("Edited iPhone")
    AdminProductsPage(browser)._click(AdminProductsPage.FIRST_PRODUCT_CHECKBOX)
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser).fill_the_product_form_with_test_data("iPhone")
    EditProductPage(browser).save_product_information()


def test_delete_product(browser):
    """Проверяет удаление продукта"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation.expand_catalog()
    AdminHomePage(browser).navigation.open_products_page()
    AdminProductsPage(browser).click_add_product()
    EditProductPage(browser).fill_the_product_form_with_test_data("test_name")
    EditProductPage(browser).save_product_information()
    AdminProductsPage(browser).delete_product("test_name")
    assert AdminProductsPage(browser).find_product("test_name") is False
