#!/usr/bin/env python
from page_objects import AdminLoginPage, AdminProductsPage, EditProductPage, AdminHomePage
import time


def test_add_product(selenoid):
    """Проверяет воркфлоу добавления продукта с тестовым именем "test_name", после удаляет его"""

    # time.sleep(20)
    AdminLoginPage(selenoid).admin_login(username="admin", password="admin")

    AdminHomePage(selenoid).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(selenoid).click_add_product()
    EditProductPage(selenoid) \
        .fill_the_required_product_fields("test_name") \
        .save_product_information()
    assert AdminProductsPage(selenoid).find_product("test_name") == "test_name"
    AdminProductsPage(selenoid) \
        .delete_product("test_name") \
        .check_console_logs()


def test_edit_product(selenoid):
    """Проверяет редактирование продукта (изменяется его имя)"""

    AdminLoginPage(selenoid).admin_login(username="demo", password="demo")
    AdminHomePage(selenoid).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(selenoid) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .fill_the_required_product_fields("Edited iPhone") \
        .save_product_information()
    AdminProductsPage(selenoid).find_product("Edited iPhone")
    AdminProductsPage(selenoid) \
        ._click(AdminProductsPage.FIRST_PRODUCT_CHECKBOX) \
        .click_edit_product()
    EditProductPage(selenoid) \
        .fill_the_required_product_fields("iPhone") \
        .save_product_information() \
        .check_console_logs()


def test_delete_product(selenoid):
    """Проверяет удаление продукта"""

    AdminLoginPage(selenoid).admin_login(username="demo", password="demo")
    AdminHomePage(selenoid).navigation.expand_catalog()
    AdminHomePage(selenoid).navigation.open_products_page()
    AdminProductsPage(selenoid).click_add_product()
    EditProductPage(selenoid).fill_the_required_product_fields("test_name")
    EditProductPage(selenoid).save_product_information()
    AdminProductsPage(selenoid) \
        .delete_product("test_name") \
        .check_console_logs()
    assert AdminProductsPage(selenoid).find_product("test_name") is False


def test_change_product_quantity(selenoid):
    """Проверяет изменение количества продукта"""

    AdminLoginPage(selenoid).admin_login(username="demo", password="demo")
    AdminHomePage(selenoid).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(selenoid) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    original_product_quantity = AdminProductsPage(selenoid).get_product_info(AdminProductsPage.FIRST_PRODUCT_QUANTITY)
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .change_product_quantity("888") \
        .save_product_information()
    AdminProductsPage(selenoid).find_product("iPhone")
    assert AdminProductsPage(selenoid).get_product_info(AdminProductsPage.FIRST_PRODUCT_QUANTITY) == "888"
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .change_product_quantity(original_product_quantity) \
        .save_product_information() \
        .check_console_logs()


def test_change_product_price(selenoid):
    """Проверяет изменение цены продукта"""

    AdminLoginPage(selenoid).admin_login(username="demo", password="demo")
    AdminHomePage(selenoid).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(selenoid) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    original_product_price = AdminProductsPage(selenoid).get_product_info(AdminProductsPage.FIRST_PRODUCT_PRICE)
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .change_product_price("200") \
        .save_product_information()
    AdminProductsPage(selenoid).find_product("iPhone")
    assert AdminProductsPage(selenoid).get_product_info(AdminProductsPage.FIRST_PRODUCT_PRICE) == "$200.00"
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .change_product_price(original_product_price) \
        .save_product_information() \
        .check_console_logs()


def test_add_product_special_price(selenoid):
    """Проверяет добавление специальной цены продукта"""

    AdminLoginPage(selenoid).admin_login(username="demo", password="demo")
    AdminHomePage(selenoid).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(selenoid) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .add_special(priority="1", price="50") \
        .save_product_information()
    AdminProductsPage(selenoid).find_product("iPhone")
    assert AdminProductsPage(selenoid).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) == "$50.00"
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .delete_last_added_special() \
        .save_product_information() \
        .check_console_logs()


def test_delete_product_special_price(selenoid):
    """Проверяет удаление специальной цены продукта"""

    AdminLoginPage(selenoid).admin_login(username="demo", password="demo")
    AdminHomePage(selenoid).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(selenoid) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .add_special(priority="1", price="50") \
        .save_product_information()
    AdminProductsPage(selenoid).find_product("iPhone")
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .delete_last_added_special() \
        .save_product_information()
    AdminProductsPage(selenoid).find_product("iPhone")
    AdminProductsPage(selenoid).check_console_logs()
    assert AdminProductsPage(selenoid).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) is False


def test_special_priority(selenoid):
    """Проверяет установленный приоритет на специальные цены продукта"""

    AdminLoginPage(selenoid).admin_login(username="demo", password="demo")
    AdminHomePage(selenoid).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(selenoid) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .add_special(priority="2", price="50") \
        .add_special(priority="1", price="80") \
        .save_product_information()
    AdminProductsPage(selenoid).find_product("iPhone")
    assert AdminProductsPage(selenoid).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) == "$80.00"
    AdminProductsPage(selenoid).click_edit_product()
    EditProductPage(selenoid) \
        .delete_last_added_special() \
        .delete_last_added_special() \
        .save_product_information() \
        .check_console_logs()

