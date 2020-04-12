from selenium.webdriver.common.by import By
from locators import AdminLoginPage, AdminNavigation, AdminProductsList, EditProduct
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_elements_present_on_main_page(browser):
    br = browser
    br.get("http://localhost/opencart/admin/")
    wait = WebDriverWait(br, 10)
    login = br.find_element(By.CSS_SELECTOR, AdminLoginPage.USERNAME)
    login.send_keys("admin")
    password = br.find_element(By.CSS_SELECTOR, AdminLoginPage.PASSWORD)
    password.send_keys("admin")
    br.find_element(By.CSS_SELECTOR, AdminLoginPage.LOGIN).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, AdminNavigation.NAVIGATION_PANEL)))
    br.find_element(By.CSS_SELECTOR, AdminNavigation.MENU_CATALOG).click()

