from selenium.webdriver.common.by import By
from locators import AdminLoginPage, AdminNavigation, AdminProductsList, EditProduct
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def admin_login(br):
    br.get("http://localhost/opencart/admin/")
    login = br.find_element(By.CSS_SELECTOR, AdminLoginPage.USERNAME)
    login.send_keys("admin")
    password = br.find_element(By.CSS_SELECTOR, AdminLoginPage.PASSWORD)
    password.send_keys("admin")
    br.find_element(By.CSS_SELECTOR, AdminLoginPage.LOGIN).click()


def open_products_page(br):
    br.find_element(By.CSS_SELECTOR, AdminNavigation.MENU_CATALOG).click()
    br.find_element(By.CSS_SELECTOR, AdminNavigation.PRODUCTS_LIST).click()


def fill_the_products_form_with_test_data(br):
    product_name = br.find_element(By.CSS_SELECTOR, EditProduct.PRODUCT_NAME)
    product_name.send_keys("test_name")
    meta_tag = br.find_element(By.CSS_SELECTOR, EditProduct.META_TAG_TITLE)
    meta_tag.send_keys("test")
    br.find_element(By.CSS_SELECTOR, EditProduct.TAB_DATA).click()
    model_name = br.find_element(By.CSS_SELECTOR, EditProduct.MODEL_NAME)
    model_name.send_keys("test_model")


def edit_product_name(br, name):
    edit_product_button = br.find_element(By.CSS_SELECTOR, AdminProductsList.FIRST_PRODUCT_EDIT_BUTTON)
    edit_product_button.click()
    product_name = br.find_element(By.CSS_SELECTOR, EditProduct.PRODUCT_NAME)
    product_name.clear()
    product_name.send_keys(name)
    save_product_information(br)


def save_product_information(br):
    save_button = br.find_element(By.CSS_SELECTOR, EditProduct.SAVE_BUTTON)
    save_button.click()


def check_product_presence(br, product_name):
    input_product_name = br.find_element(By.CSS_SELECTOR, AdminProductsList.PRODUCT_NAME_IN_FILTER)
    input_product_name.clear()
    time.sleep(10)
    input_product_name.send_keys(product_name)
    br.find_element(By.CSS_SELECTOR, AdminProductsList.FILTER_BUTTON).click()
    found_product = br.find_element(By.CSS_SELECTOR, AdminProductsList.FIRST_PRODUCT_IN_THE_LIST)
    print(found_product.text)
    assert found_product.text == product_name


def test_add_product(browser):
    br = browser
    br.maximize_window()
    wait = WebDriverWait(br, 10)
    admin_login(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, AdminNavigation.NAVIGATION_PANEL)))
    open_products_page(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, AdminProductsList.ADD_PRODUCT)))
    try:
        br.find_element(By.CSS_SELECTOR, AdminProductsList.ADD_PRODUCT).click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, EditProduct.FORM_PRODUCT)))
        fill_the_products_form_with_test_data(br)
        save_product_information(br)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, AdminProductsList.FILTER_PRODUCT_FORM)))
        check_product_presence(br, "test_name")
    finally:
        if check_product_presence(br, "test_name"):
            product_checkbox = br.find_element(By.CSS_SELECTOR, AdminProductsList.FIRST_PRODUCT_CHECKBOX)
            product_checkbox.click()
            br.find_element(By.CSS_SELECTOR, AdminProductsList.DELETE_PRODUCT).click()


def test_edit_product(browser):
    br = browser
    br.maximize_window()
    wait = WebDriverWait(br, 10)
    admin_login(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, AdminNavigation.NAVIGATION_PANEL)))
    open_products_page(br)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, AdminProductsList.FILTER_PRODUCT_FORM)))
    time.sleep(10)
    try:
        check_product_presence(br, "iPhone")
        time.sleep(10)
        product_checkbox = br.find_element(By.CSS_SELECTOR, AdminProductsList.FIRST_PRODUCT_CHECKBOX)
        product_checkbox.click()
        edit_product_name(br, "Edited iMac")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, AdminProductsList.FILTER_PRODUCT_FORM)))
        check_product_presence(br, "Edited iMac")
    finally:
        if check_product_presence(br, "Edited iMac"):
            product_checkbox = br.find_element(By.CSS_SELECTOR, AdminProductsList.FIRST_PRODUCT_CHECKBOX)
            product_checkbox.click()
            edit_product_name(br, "iMac")















