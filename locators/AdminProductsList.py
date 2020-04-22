#!/usr/bin/env python
class AdminProductsList:
    """Локаторы для страницы администрирования продуктов"""

    ADD_PRODUCT = "a[data-original-title='Add New']"
    COPY_PRODUCT = "button[data-original-title='Copy']"
    DELETE_PRODUCT = "button[data-original-title='Delete']"
    FILTER_PRODUCT_FORM = "div > #filter-product "
    PRODUCT_NAME_IN_FILTER = "div > #filter-product  #input-name"
    FILTER_BUTTON = "div > #filter-product  #button-filter"
    FIRST_PRODUCT_IN_THE_LIST = "#form-product > div > table > tbody > tr > td:nth-child(3)"
    FIRST_PRODUCT_CHECKBOX = "#form-product > div > table > tbody > tr > td:nth-child(1) >\
        input[type=checkbox]"
    FIRST_PRODUCT_EDIT_BUTTON = "#form-product > div > table > tbody > tr > td:nth-child(8)\
        > a > i"
