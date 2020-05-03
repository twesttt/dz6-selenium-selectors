#!/usr/bin/env python
from page_objects import AdminLoginPage, AdminProductsPage, EditProductPage, AdminHomePage


def test_add_product(remote):
    """Проверяет воркфлоу добавления продукта с тестовым именем "test_name", после удаляет его"""

    AdminLoginPage(remote).admin_login(username="admin", password="admin")

    AdminHomePage(remote).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(remote).click_add_product()
    EditProductPage(remote) \
        .fill_the_required_product_fields("test_name") \
        .save_product_information()
    assert AdminProductsPage(remote).find_product("test_name") == "test_name"
    AdminProductsPage(remote) \
        .delete_product("test_name") \
        .check_console_logs()


def test_edit_product(remote):
    """Проверяет редактирование продукта (изменяется его имя)"""

    AdminLoginPage(remote).admin_login(username="admin", password="admin")
    AdminHomePage(remote).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(remote) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .fill_the_required_product_fields("Edited iPhone") \
        .save_product_information()
    AdminProductsPage(remote).find_product("Edited iPhone")
    AdminProductsPage(remote) \
        ._click(AdminProductsPage.FIRST_PRODUCT_CHECKBOX) \
        .click_edit_product()
    EditProductPage(remote) \
        .fill_the_required_product_fields("iPhone") \
        .save_product_information() \
        .check_console_logs()


def test_delete_product(remote):
    """Проверяет удаление продукта"""

    AdminLoginPage(remote).admin_login(username="admin", password="admin")
    AdminHomePage(remote).navigation.expand_catalog()
    AdminHomePage(remote).navigation.open_products_page()
    AdminProductsPage(remote).click_add_product()
    EditProductPage(remote).fill_the_required_product_fields("test_name")
    EditProductPage(remote).save_product_information()
    AdminProductsPage(remote) \
        .delete_product("test_name") \
        .check_console_logs()
    assert AdminProductsPage(remote).find_product("test_name") is False


def test_change_product_quantity(remote):
    """Проверяет изменение количества продукта"""

    AdminLoginPage(remote).admin_login(username="admin", password="admin")
    AdminHomePage(remote).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(remote) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    original_product_quantity = AdminProductsPage(remote).get_product_info(AdminProductsPage.FIRST_PRODUCT_QUANTITY)
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .change_product_quantity("888") \
        .save_product_information()
    AdminProductsPage(remote).find_product("iPhone")
    assert AdminProductsPage(remote).get_product_info(AdminProductsPage.FIRST_PRODUCT_QUANTITY) == "888"
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .change_product_quantity(original_product_quantity) \
        .save_product_information() \
        .check_console_logs()


def test_change_product_price(remote):
    """Проверяет изменение цены продукта"""

    AdminLoginPage(remote).admin_login(username="admin", password="admin")
    AdminHomePage(remote).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(remote) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    original_product_price = AdminProductsPage(remote).get_product_info(AdminProductsPage.FIRST_PRODUCT_PRICE)
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .change_product_price("200") \
        .save_product_information()
    AdminProductsPage(remote).find_product("iPhone")
    assert AdminProductsPage(remote).get_product_info(AdminProductsPage.FIRST_PRODUCT_PRICE) == "$200.00"
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .change_product_price(original_product_price) \
        .save_product_information() \
        .check_console_logs()


def test_add_product_special_price(remote):
    """Проверяет добавление специальной цены продукта"""

    AdminLoginPage(remote).admin_login(username="admin", password="admin")
    AdminHomePage(remote).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(remote) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .add_special(priority="1", price="50") \
        .save_product_information()
    AdminProductsPage(remote).find_product("iPhone")
    assert AdminProductsPage(remote).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) == "$50.00"
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .delete_last_added_special() \
        .save_product_information() \
        .check_console_logs()


def test_delete_product_special_price(remote):
    """Проверяет удаление специальной цены продукта"""

    AdminLoginPage(remote).admin_login(username="admin", password="admin")
    AdminHomePage(remote).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(remote) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .add_special(priority="1", price="50") \
        .save_product_information()
    AdminProductsPage(remote).find_product("iPhone")
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .delete_last_added_special() \
        .save_product_information()
    AdminProductsPage(remote).find_product("iPhone")
    AdminProductsPage(remote).check_console_logs()
    assert AdminProductsPage(remote).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) is False


def test_special_priority(remote):
    """Проверяет установленный приоритет на специальные цены продукта"""

    AdminLoginPage(remote).admin_login(username="admin", password="admin")
    AdminHomePage(remote).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(remote) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .add_special(priority="2", price="50") \
        .add_special(priority="1", price="80") \
        .save_product_information()
    AdminProductsPage(remote).find_product("iPhone")
    assert AdminProductsPage(remote).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) == "$80.00"
    AdminProductsPage(remote).click_edit_product()
    EditProductPage(remote) \
        .delete_last_added_special() \
        .delete_last_added_special() \
        .save_product_information() \
        .check_console_logs()

