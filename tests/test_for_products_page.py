#!/usr/bin/env python
from page_objects import AdminLoginPage, AdminProductsPage, EditProductPage, AdminHomePage


def test_add_product(cloud):
    """Проверяет воркфлоу добавления продукта с тестовым именем "test_name", после удаляет его"""

    AdminLoginPage(cloud).admin_login(username="demo", password="demo")

    AdminHomePage(cloud).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(cloud).click_add_product()
    EditProductPage(cloud) \
        .fill_the_required_product_fields("test_name") \
        .save_product_information()
    assert AdminProductsPage(cloud).find_product("test_name") == "test_name"
    AdminProductsPage(cloud) \
        .delete_product("test_name") \
        .check_console_logs()


def test_edit_product(cloud):
    """Проверяет редактирование продукта (изменяется его имя)"""

    AdminLoginPage(cloud).admin_login(username="demo", password="demo")
    AdminHomePage(cloud).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(cloud) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .fill_the_required_product_fields("Edited iPhone") \
        .save_product_information()
    AdminProductsPage(cloud).find_product("Edited iPhone")
    AdminProductsPage(cloud) \
        ._click(AdminProductsPage.FIRST_PRODUCT_CHECKBOX) \
        .click_edit_product()
    EditProductPage(cloud) \
        .fill_the_required_product_fields("iPhone") \
        .save_product_information() \
        .check_console_logs()


def test_delete_product(cloud):
    """Проверяет удаление продукта"""

    AdminLoginPage(cloud).admin_login(username="demo", password="demo")
    AdminHomePage(cloud).navigation.expand_catalog()
    AdminHomePage(cloud).navigation.open_products_page()
    AdminProductsPage(cloud).click_add_product()
    EditProductPage(cloud).fill_the_required_product_fields("test_name")
    EditProductPage(cloud).save_product_information()
    AdminProductsPage(cloud) \
        .delete_product("test_name") \
        .check_console_logs()
    assert AdminProductsPage(cloud).find_product("test_name") is False


def test_change_product_quantity(cloud):
    """Проверяет изменение количества продукта"""

    AdminLoginPage(cloud).admin_login(username="demo", password="demo")
    AdminHomePage(cloud).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(cloud) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    original_product_quantity = AdminProductsPage(cloud).get_product_info(AdminProductsPage.FIRST_PRODUCT_QUANTITY)
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .change_product_quantity("888") \
        .save_product_information()
    AdminProductsPage(cloud).find_product("iPhone")
    assert AdminProductsPage(cloud).get_product_info(AdminProductsPage.FIRST_PRODUCT_QUANTITY) == "888"
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .change_product_quantity(original_product_quantity) \
        .save_product_information() \
        .check_console_logs()


def test_change_product_price(cloud):
    """Проверяет изменение цены продукта"""

    AdminLoginPage(cloud).admin_login(username="demo", password="demo")
    AdminHomePage(cloud).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(cloud) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    original_product_price = AdminProductsPage(cloud).get_product_info(AdminProductsPage.FIRST_PRODUCT_PRICE)
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .change_product_price("200") \
        .save_product_information()
    AdminProductsPage(cloud).find_product("iPhone")
    assert AdminProductsPage(cloud).get_product_info(AdminProductsPage.FIRST_PRODUCT_PRICE) == "$200.00"
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .change_product_price(original_product_price) \
        .save_product_information() \
        .check_console_logs()


def test_add_product_special_price(cloud):
    """Проверяет добавление специальной цены продукта"""

    AdminLoginPage(cloud).admin_login(username="demo", password="demo")
    AdminHomePage(cloud).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(cloud) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .add_special(priority="1", price="50") \
        .save_product_information()
    AdminProductsPage(cloud).find_product("iPhone")
    assert AdminProductsPage(cloud).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) == "$50.00"
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .delete_last_added_special() \
        .save_product_information() \
        .check_console_logs()


def test_delete_product_special_price(cloud):
    """Проверяет удаление специальной цены продукта"""

    AdminLoginPage(cloud).admin_login(username="demo", password="demo")
    AdminHomePage(cloud).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(cloud) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .add_special(priority="1", price="50") \
        .save_product_information()
    AdminProductsPage(cloud).find_product("iPhone")
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .delete_last_added_special() \
        .save_product_information()
    AdminProductsPage(cloud).find_product("iPhone")
    AdminProductsPage(cloud).check_console_logs()
    assert AdminProductsPage(cloud).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) is False


def test_special_priority(cloud):
    """Проверяет установленный приоритет на специальные цены продукта"""

    AdminLoginPage(cloud).admin_login(username="demo", password="demo")
    AdminHomePage(cloud).navigation \
        .expand_catalog() \
        .open_products_page()
    AdminProductsPage(cloud) \
        ._wait_for_visible(AdminProductsPage.FILTER_PRODUCT_FORM) \
        .find_product("iPhone")
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .add_special(priority="2", price="50") \
        .add_special(priority="1", price="80") \
        .save_product_information()
    AdminProductsPage(cloud).find_product("iPhone")
    assert AdminProductsPage(cloud).get_product_info(AdminProductsPage.FIRST_PRODUCT_SPECIAL_PRICE) == "$80.00"
    AdminProductsPage(cloud).click_edit_product()
    EditProductPage(cloud) \
        .delete_last_added_special() \
        .delete_last_added_special() \
        .save_product_information() \
        .check_console_logs()

