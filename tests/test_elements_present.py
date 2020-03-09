from selenium.webdriver.common.by import By

from locators import MainPage, ProductPage


def test_elements_present_main_page(browser):
    br = browser
    br.find_element_by_class_name(MainPage.PROMOBLOCK)
    br.find_element_by_css_selector(MainPage.SEARCH_INPUT)
    br.find_element_by_css_selector(MainPage.SEARCH_BUTTON)
    br.find_element_by_link_text(MainPage.DESKTOPS_MENU)
    br.find_element(By.LINK_TEXT, MainPage.LAPTOPS_MENU)
    br.find_element(By.LINK_TEXT, MainPage.COMPONENTS_MENU)
    br.find_element_by_css_selector(MainPage.SLIDE_NEXT)
    br.find_element_by_css_selector(MainPage.ADD_TO_WISH_LIST)


def test_elements_present_product_page(browser):
    br = browser.get("http://localhost/opencart/index.php?route=product/product&product_id=43")