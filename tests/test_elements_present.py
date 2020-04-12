from selenium.webdriver.common.by import By
from locators import MainPage, ProductPage, SearchPage, Catalog, AdminLoginPage


def test_elements_present_on_main_page(browser):
    br = browser
    br.find_element_by_class_name(MainPage.PROMOBLOCK)
    br.find_element_by_css_selector(MainPage.SEARCH_INPUT)
    br.find_element_by_css_selector(MainPage.SEARCH_BUTTON)
    br.find_element_by_link_text(MainPage.DESKTOPS_MENU)
    br.find_element(By.LINK_TEXT, MainPage.LAPTOPS_MENU)
    br.find_element(By.LINK_TEXT, MainPage.COMPONENTS_MENU)
    br.find_element_by_css_selector(MainPage.SLIDE_NEXT)
    br.find_element_by_css_selector(MainPage.ADD_TO_WISH_LIST)


def test_elements_present_on_product_page(browser):
    br = browser
    br.get("http://localhost/opencart/index.php?route=product/product&product_id=43")
    br.find_element_by_css_selector(ProductPage.ADD_TO_CART)
    br.find_element_by_css_selector(ProductPage.INPUT_QUANTITY)
    br.find_element_by_css_selector(ProductPage.REVIEWS)
    br.find_element_by_css_selector(ProductPage.SPECIFICATION)
    br.find_element_by_css_selector(ProductPage.IMAGE)


def test_elements_present_on_catalog_page(browser):
    br = browser
    br.get("http://localhost/opencart/index.php?route=product/category&path=33")
    br.find_element_by_css_selector(Catalog.GRID_VIEW)
    br.find_element_by_css_selector(Catalog.PRODUCT_COMPARE)
    br.find_element_by_css_selector(Catalog.LIST_VIEW)
    br.find_element_by_css_selector(Catalog.SORT_BY)
    br.find_element_by_css_selector(Catalog.HOME)


def test_elements_present_on_admin_page(browser):
    br = browser
    br.get("http://localhost/opencart/admin/")
    br.find_element(By.ID, AdminLoginPage.USERNAME)
    br.find_element(By.ID, AdminLoginPage.PASSWORD)
    br.find_element_by_css_selector(AdminLoginPage.FORGOTTEN_PASSWORD)
    br.find_element_by_css_selector(AdminLoginPage.LOGIN)
    br.find_element_by_css_selector(AdminLoginPage.OPEN_CART)


def test_elements_present_on_search_page(browser):
    br = browser
    br.get("http://localhost/opencart/index.php?route=product/search&search=phone")
    br.find_element(By.ID, SearchPage.INPUT_SEARCH)
    br.find_element(By.ID, SearchPage.SEARCH_IN_DESCRIPTION)
    br.find_element(By.ID, SearchPage.SEARCH_BUTTON)
    br.find_element_by_css_selector(SearchPage.CATEGORIES)
    br.find_element_by_css_selector(SearchPage.SEARCH_IN_SUBCATEGORIES)

