#!/usr/bin/env python
from page_objects import AdminLoginPage, AdminProductsPage, EditProductPage, AdminHomePage


def test_add_product(browser):
    """Проверяет воркфлоу добавления продукта с тестовым именем "test_name", после удаляет его"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")

    AdminHomePage(browser).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(browser).click_add_product()
    EditProductPage(browser) \
        .fill_the_required_product_fields("test_name") \
        .save_product_information()
    assert AdminProductsPage(browser).find_product("test_name") == "test_name"
    AdminProductsPage(browser) \
        .delete_product("test_name") \
        .check_console_logs()


def test_edit_product(browser):
    """Проверяет редактирование продукта (изменяется его имя)"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(browser) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .fill_the_required_product_fields("Edited iPhone") \
        .save_product_information()
    AdminProductsPage(browser).find_product("Edited iPhone")
    AdminProductsPage(browser) \
        ._click(AdminProductsPage.FIRST_PRODUCT_CHECKBOX) \
        .click_edit_product()
    EditProductPage(browser) \
        .fill_the_required_product_fields("iPhone") \
        .save_product_information() \
        .check_console_logs()


def test_delete_product(browser):
    """Проверяет удаление продукта"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation.expand_catalog()
    AdminHomePage(browser).navigation.open_products_page()
    AdminProductsPage(browser).click_add_product()
    EditProductPage(browser).fill_the_required_product_fields("test_name")
    EditProductPage(browser).save_product_information()
    AdminProductsPage(browser) \
        .delete_product("test_name") \
        .check_console_logs()
    assert AdminProductsPage(browser).find_product("test_name") is False


def test_change_product_quantity(browser):
    """Проверяет изменение количества продукта"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(browser) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    original_product_quantity = AdminProductsPage(browser).get_product_info(AdminProductsPage.FIRST_PRODUCT_QUANTITY)
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .change_product_quantity("888") \
        .save_product_information()
    AdminProductsPage(browser).find_product("iPhone")
    assert AdminProductsPage(browser).get_product_info(AdminProductsPage.FIRST_PRODUCT_QUANTITY) == "888"
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .change_product_quantity(original_product_quantity) \
        .save_product_information() \
        .check_console_logs()


def test_change_product_price(browser):
    """Проверяет изменение цены продукта"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(browser) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    original_product_price = AdminProductsPage(browser).get_product_info(AdminProductsPage.FIRST_PRODUCT_PRICE)
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .change_product_price("200") \
        .save_product_information()
    AdminProductsPage(browser).find_product("iPhone")
    assert AdminProductsPage(browser).get_product_info(AdminProductsPage.FIRST_PRODUCT_PRICE) == "$200.00"
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .change_product_price(original_product_price) \
        .save_product_information() \
        .check_console_logs()


def test_add_product_special_price(browser):
    """Проверяет добавление специальной цены продукта"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(browser) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .add_special(priority="1", price="50") \
        .save_product_information()
    AdminProductsPage(browser).find_product("iPhone")
    assert AdminProductsPage(browser).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) == "$50.00"
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .delete_last_added_special() \
        .save_product_information() \
        .check_console_logs()


def test_delete_product_special_price(browser):
    """Проверяет удаление специальной цены продукта"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(browser) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .add_special(priority="1", price="50") \
        .save_product_information()
    AdminProductsPage(browser).find_product("iPhone")
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .delete_last_added_special() \
        .save_product_information()
    AdminProductsPage(browser).find_product("iPhone")
    AdminProductsPage(browser).check_console_logs()
    assert AdminProductsPage(browser).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) is False


def test_special_priority(browser):
    """Проверяет установленный приоритет на специальные цены продукта"""

    AdminLoginPage(browser).admin_login(username="admin", password="admin")
    AdminHomePage(browser).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(browser) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .add_special(priority="2", price="50") \
        .add_special(priority="1", price="80") \
        .save_product_information()
    AdminProductsPage(browser).find_product("iPhone")
    assert AdminProductsPage(browser).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) == "$80.00"
    AdminProductsPage(browser).click_edit_product()
    EditProductPage(browser) \
        .delete_last_added_special() \
        .delete_last_added_special() \
        .save_product_information() \
        .check_console_logs()

